import requests
from jsonpath_rw import jsonpath, parse

class TellAJoke():
  def handleCommand(self, command):
    headers = {
        'User-Agent': 'python:mitybot:v1.0 (by /u/4A18B156)'
    }
    try:
      resp = requests.get("https://www.reddit.com/r/Jokes/hot.json", headers=headers)
    except:
      return "An error occurred"
    #print resp.text
    resp = resp.json()
    idx = 0
    while True:
        stickied = parse('$.data.children[{0}].data.stickied'.format(idx)).find(resp)
        if stickied[0].value == False:
            break
        idx = idx + 1
    print "idx is ", idx
    title = parse('$.data.children[{0}].data.title'.format(idx)).find(resp)
    selftext = parse('$.data.children[{0}].data.selftext'.format(idx)).find(resp)
    print title
    print selftext
    if not title or not selftext:
      return "An error occurred"
    title = title[0].value
    selftext = selftext[0].value
    return u"Here's the top joke from reddit:\n{0}\n\n{1}".format(title, selftext)
