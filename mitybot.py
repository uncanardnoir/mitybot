import argparse
import requests
import json
import re
import time
import urllib
import PIL
from PIL import JpegImagePlugin
from io import BytesIO
from command_handler import CommandHandler
from jsonpath_rw import jsonpath, parse
import sys

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

  def replyImage(self, result, image, optionalText=None, nonotify=True):
    chatId = parse('$.message.chat.id').find(result)
    if chatId:
      image_file = BytesIO()
      image.save(image_file, "JPEG")
      image_file.seek(0)
      multipart_data = {
        "chat_id": ('', str(chatId[0].value)),
        "photo": image_file
      }
      requests.post('https://api.telegram.org/bot{0}/sendPhoto'.format(self.apiKey), files=multipart_data)

  def replyImageLink(self, result, link, optionalText=None, nonotify=True):
    chatId = parse('$.message.chat.id').find(result)
    if chatId:
      embeddedUrl = urllib.quote_plus(link)
      requests.post('https://api.telegram.org/bot{0}/sendPhoto?chat_id={1}&photo={2}'.format(self.apiKey, str(chatId[0].value), embeddedUrl))

  def replyDocumentLink(self, result, link, optionalText=None, nonotify=True):
    chatId = parse('$.message.chat.id').find(result)
    if chatId:
      embeddedUrl = urllib.quote_plus(link)
      requests.post('https://api.telegram.org/bot{0}/sendDocument?chat_id={1}&document={2}'.format(self.apiKey, str(chatId[0].value), embeddedUrl))

  def handleChatMemberJoin(self, result):
    newMember = parse('$.message.new_chat_participant.id').find(result)
    if newMember and newMember[0].value != 435893184: # Don't welcome ourselves... that's just tacky
      newMemberName = parse('$.message.new_chat_participant.first_name').find(result)
      chatName = parse('$.message.chat.title').find(result)
      if not newMemberName or not chatName:
        return
      welcomeMsg = 'Welcome to {0}, {1}! The message of the day is <getMotdHandler.Mitybot instance at 0x7f2524f1f998>.\n\n(I am Mitybot 2.0, and I am being tested in production! Go me!)'.format(newMemberName[0].value, chatName[0].value)
      self.replyText(result, welcomeMsg)

  def handleMessage(self, result):
    # in group chats, ignore commands not beginning with /mitybot
    groupType = parse('$.message.chat.type').find(result)
    text = parse('$.message.text').find(result)
    if not text:
      return
    text = text[0].value
    if groupType and groupType[0].value == "group":
      if text and not text.lower().startswith('/mitybot '):
        return False
      text = text[9:]
    
    ret = self.commandHandler.handleCommand(result, text)
    print "got back:", ret
    if not ret:
      return
    if isinstance(ret, basestring):
      self.replyText(result, ret)
    elif isinstance(ret, PIL.JpegImagePlugin.JpegImageFile):
      self.replyImage(result, ret)
    elif isinstance(ret, tuple):
      if ret[0] == 'documentLink':
        self.replyDocumentLink(result, ret[1])
      if ret[0] == 'imageLink':
        self.replyImageLink(result, ret[1])

  def start(self):
    self.commandHandler = CommandHandler()
    with open('private/telegramApiKey', 'r') as apiKeyFile:
      self.apiKey = apiKeyFile.read().replace('\n', '')
    with open('private/chatWhitelist', 'r') as chatWhitelistFile:
      self.chatWhitelist = json.loads(stripComments(chatWhitelistFile.read()))
    with open('private/userBlacklist', 'r') as userBlacklistFile:
      self.userBlacklist = json.loads(stripComments(userBlacklistFile.read()))

    curOffset = 0
    while True:
      getUpdatesUrl = 'https://api.telegram.org/bot{0}/getUpdates?offset={1}'.format(self.apiKey, curOffset + 1)
      resp = requests.get(getUpdatesUrl)
      resp = json.loads(resp.text)
      for result in resp["result"]:
        resultId = parse('$.update_id').find(result)
        if resultId and resultId[0].value > curOffset:
          curOffset = resultId[0].value
        if not self.checkEligibility(result):
          continue
        self.handleChatMemberJoin(result)
        self.handleMessage(result)
      time.sleep(1)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Start server')
  parser.add_argument('--k', dest='kill', action='store_true')
  args = parser.parse_args()
  if args.kill:
    print "not impl"
  mitybot = Mitybot()
  exit(mitybot.start())
