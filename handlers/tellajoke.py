import requests
from jsonpath_rw import jsonpath, parse

class TellAJoke():
  def handleCommand(self, command):
    headers = {
        'User-Agent': 'python:mitybot:v1.0 (by /u/4A18B156)'
    }
    try:
      resp = requests.get("https://www.reddit.com/r/Jokes/hot.json?limit=1", headers=headers)
    except:
      return "An error occurred"
    print resp.text
    resp = resp.json()
    title = parse('$.data.children[0].data.title').find(resp)
    selftext = parse('$.data.children[0].data.selftext').find(resp)
    print title
    print selftext
    if not title or not selftext:
      return "An error occurred"
    title = title[0].value
    selftext = selftext[0].value
    return "Here's the top joke from reddit:\n{0}\n\n{1}".format(title, selftext)
