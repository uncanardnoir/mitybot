import time
from platform import platform

class Whoareyou():
  def __init__(self):
    self.startTime = time.time()
    self.platform = platform()

  def setLover(self, lover):
    self.lover = lover

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

  def handleCommand(self, command):
#    ret = 'I am MityBot 2.0, running on {0}, in the cloud! I have been up for {1}. I am pleased to be your Mity-as-a-service provider! I am gluten free, organic and free trade, free range non-GMO kosher vegan, low fat, low sodium no MSG no added sugar and never, ever any antibiotics. Type \"/mitybot help\" (without the quotes) to see what I can do!\n\n{2}\nI am active on and whitelisting 2 groups:\nFucking Memellennials\nCat++ Chat 2017'.format(self.platform, self.getUptime(), self.lover.getLoveString())
    ret = 'I am MityBot 2.0, running on {0}, in the cloud! I have been up for {1}. I am pleased to be your Mity-as-a-service provider! I am gluten free, organic and free trade, free range non-GMO kosher vegan, low fat, low sodium no MSG no added sugar and never, ever any antibiotics. Type \"/mitybot help\" (without the quotes) to see what I can do!\n\n{2}\nI am active on and whitelisting 12 groups:\nFucking Memellennials\nRyan Appreciation Thread\nCorncendants 4: A New Pop\nAsian Persuasian\nAriana Grande Fanclub\nBotDevLeadsEx\nCat++ Chat 2017\nRogue One\nNotice Me Sempai\nNY Events\nFinance Bros II: More Alpha\nBDSM Tips & Tutorials\nStill Sad Panda'.format(self.platform, self.getUptime(), self.lover.getLoveString())
    return ret
