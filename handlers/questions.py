import urllib2

class Question():
  def __init__(self):
    self.apikey = "P9QH7H-JPE2YVUA8W"

  def handleCommand(self, command):
    try:
      content = urllib2.urlopen(self.getWolframString(urllib2.quote(command.args))).read()
    except:
      content = "I'm sorry I don't know the answer to that"
    return content

  def getWolframString(self, cmd):
    #combine the parsed command with the wolfram string and api keys
    return "https://api.wolframalpha.com/v1/result?i={0}&appid={1}".format(cmd,self.apikey)