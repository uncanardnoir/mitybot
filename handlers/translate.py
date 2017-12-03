import requests
import urllib

class Translate():
  def handleCommand(self, command):
    split = command.args.split(" ", 1)
    if len(split) < 2:
      return "Invalid input"
    tarLang = split[0]
    transStr = split[1]
    transStr = urllib.quote_plus(transStr.encode('utf-8'))
    try:
      resp = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={0}&dt=t&q={1}".format(tarLang, transStr))
      resp = resp.json()[0][0][0]
    except:
      return "An error occurred"
    return resp
