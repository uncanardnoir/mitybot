import argparse
import requests
import json
import re
import urllib
import command_handler
from jsonpath_rw import jsonpath, parse

def stripComments(inStr):
  return re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", inStr)

class Mitybot:
  def checkEligibility(self, result):
    # is user blacklisted
    userId = parse('$.message.from.id').find(result)
    if userId and userId[0].value in self.userBlacklist:
      return False

    # no bots!
    isBot = parse('$.message.from.is_bot').find(result)
    if isBot and isBot[0].value == True:
      return False

    # is chat whitelisted
    chatId = parse('$.message.chat.id').find(result)
    if chatId and not chatId[0].value in self.chatWhitelist:
      return False

    return True

  def replyText(self, result, text, nonotify = True):
    chatId = parse('$.message.chat.id').find(result)
    if chatId:
      textencoded = urllib.quote_plus(text)
      nonotify = "&disable_notification=true" if nonotify else ""
      url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}{3}'.format(self.apiKey, chatId[0].value, textencoded, nonotify)
      requests.get(url)

  def handleChatMemberJoin(self, result):
    newMember = parse('$.message.new_chat_participant.id').find(result)
    if newMember and newMember[0].value != 435893184: # Don't welcome ourselves... that's just tacky
      newMemberName = parse('$.message.new_chat_participant.first_name').find(result)
      chatName = parse('$.message.chat.title').find(result)
      if not newMemberName or not chatName:
        return
      welcomeMsg = 'Welcome to {0}, {1}! The message of the day is {{3}}.\n\n(I am Mitybot 2.0, and I am being tested in production! Go me!)'.format(newMemberName[0].value, chatName[0].value)
      self.replyText(result, welcomeMsg)

  def handleMessage(self, result):
    # in group chats, ignore commands not beginning with /mitybot
    groupType = parse('$.message.chat.type').find(result)
    text = parse('$.message.text').find(result)
    if groupType and groupType[0].value == "group":
      if text and not text[0].value.lower().startswith('/mitybot '):
        return False
      text = text[9:]
    handleCommand(self, result, command)

  def start(self):
    with open('private/telegramApiKey', 'r') as apiKeyFile:
      self.apiKey = apiKeyFile.read().replace('\n', '')
    with open('private/chatWhitelist', 'r') as chatWhitelistFile:
      self.chatWhitelist = json.loads(stripComments(chatWhitelistFile.read()))
    with open('private/userBlacklist', 'r') as userBlacklistFile:
      self.userBlacklist = json.loads(stripComments(userBlacklistFile.read()))

    curOffset = 0
    getUpdatesUrl = 'https://api.telegram.org/bot{0}/getUpdates?offset={1}'.format(self.apiKey, curOffset)
    print getUpdatesUrl
    resp = requests.get(getUpdatesUrl)
    resp = json.loads(resp.text)
    for result in resp["result"]:
      if not self.checkEligibility(result):
        continue
      self.handleChatMemberJoin(result)
      self.handleMessage(result)
      self.replyText(result, "The quick brown fox jumped over the lazy dog!!&")
      #print result

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Start server')
  parser.add_argument('--k', dest='kill', action='store_true')
  args = parser.parse_args()
  if args.kill:
    print "not impl"
  mitybot = Mitybot()
  exit(mitybot.start())
