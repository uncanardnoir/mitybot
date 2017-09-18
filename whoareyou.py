import time
from platform import platform

class Whoareyou():
  def __init__(self):
    self.startTime = time.time()
    self.platform = platform()

  def getUptime(self):
    elapsed = time.time() - self.startTime
    if elapsed < 60:
      return '{0} seconds'.format(int(elapsed))
    elapsed /= 60
    if elapsed < 60:
      return '{0} minutes'.format(int(elapsed))
    elapsed /= 60
    if elapsed < 60:
      return '{0} hours'.format(int(elapsed))
    elapsed /= 24
    return '{0} days'.format(int(elapsed))

  def handleCommand(self, args):
    ret = 'I am MityBot 2.0, running on {0}, in the cloud! I have been up for {1}. I am pleased to be your Mity-as-a-service provider!\n\nI have been loved 0 times :(\n\nI am active on and whitelisting 12 groups:\nFucking Memellennials\nRyan Appreciation Thread\nCorncendants 4: A New Pop\nAsian Persuasian\nAriana Grande Fanclub\nBotDevLeadsEx\nCat++ Chat 2017\nRogue One\nNotice Me Sempai\nNY Events\nFinance Bros II: More Alpha\nBDSM Tips & Tutorials'.format(self.platform, self.getUptime())
    return ret
