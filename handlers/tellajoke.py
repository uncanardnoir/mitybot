import requests
from jsonpath_rw import jsonpath, parse

class TellAJoke():
  def handleCommand(self, command):
    try:
      resp = requests.get("https://www.reddit.com/r/Jokes/hot.json?limit=1")
    except:
      return "An error occurred"
    resp = resp.json()
    title = parse('$.data.children[0].data.title').find(resp)
    selftext = parse('$.data.children[0].data.selftext').find(resp)
    if not title or not selftext:
      return "An error occurred"
    title = title[0].value
    selftext = selftext[0].value
    return "Here's the top joke from reddit:\n*{0}*\n{1}".format(title, selftext)
