import argparse
import requests
import json
import urllib

httpsPort = 8443

def doCreateWebhook(silent = False):
  with open('private/telegramApiKey', 'r') as apiKeyFile:
    apiKey = apiKeyFile.read().replace('\n', '')
  with open('private/externalIp', 'r') as publicIpFile:
    publicIp = publicIpFile.read().replace('\n', '')

  # Init callback url
  callbackUrl = 'https://{0}:{1}/{2}'.format(publicIp, httpsPort, apiKey)
  if not silent:
    print 'Callback url is', callbackUrl
  callbackUrl = urllib.quote_plus(callbackUrl)

  # Init public cert file
  files = {'certificate': open('cert/cert.pem', 'rb'),
    'url': callbackUrl}

  url = 'https://api.telegram.org/bot{0}/setWebhook'.format(apiKey)
  if not silent:
    print 'Executing GET request:', url
  r = requests.post(url, files=files)
  if not silent:
    print r.status_code
  if not silent:
    print r.content
  if r.status_code != 200:
    return -1
  j = json.loads(r.content)
  if not isinstance(j, dict) or not "ok" in j or not "result" in j or j["ok"] != True or j["result"] != True:
    return -1
  return 0 

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Creates telegram webhook')
  parser.add_argument('--silent', dest='silent', action='store_true')
  args = parser.parse_args()
  exit(doCreateWebhook(args.silent))
