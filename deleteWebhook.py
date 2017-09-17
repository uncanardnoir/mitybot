import argparse
import requests
import json

def doDeleteWebhook(silent = False):
  with open('private/telegramApiKey', 'r') as apiKeyFile:
    apiKey = apiKeyFile.read().replace('\n', '')

  url = 'https://api.telegram.org/bot{0}/deleteWebhook'.format(apiKey)
  if not silent:
    print 'Executing GET request:', url
  r = requests.get(url)
  if not silent:
    print r.status_code
  if r.status_code != 200:
    return -1
  if not silent:
    print r.content
  j = json.loads(r.content)
  if not isinstance(j, dict) or not "ok" in j or not "result" in j or j["ok"] != True or j["result"] != True:
    return -1
  return 0 

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Deletes telegram webhook')
  parser.add_argument('--silent', dest='silent', action='store_true')
  args = parser.parse_args()
  exit(doDeleteWebhook(args.silent))
