import os
from jsonpath_rw import jsonpath, parse

class ILoveYou():
  def handleCommand(self, command):
    userId = parse('$.message.from.id').find(command.parent)
    userFirstname = parse('$.message.from.first_name').find(command.parent)
    if not userId or not userFirstname:
      return None
    userId = userId[0].value
    userFirstname = userFirstname[0].value
    userFile = 'love/{0}'.format(userId)
    if not os.path.isfile(userFile):
      with open(userFile, "w") as f:
        f.write("{0}\n1".format(userFirstname))
    else:
      with open(userFile, "r+") as f:
        data = f.read().split()
        nLoves = int(data[1]) + 1
        f.seek(0)
        f.write("{0}\n{1}".format(userFirstname, nLoves))
        f.truncate()
    return "I love you too bbg <3"

  def getLoveString(self):
    ret = ''
    nLoves = 0
    for filepath in os.listdir('love'):
      with open(os.path.join('love', filepath), "r") as f:
        data = f.read().split()
        thisLove = int(data[1])
        thisName = data[0]
        thisline = '{0} time{2} from {1}\n'.format(thisLove, thisName, 's' if thisLove != 1 else '')
        ret += thisline
        nLoves = nLoves + thisLove
    if nLoves == 0:
      return 'I have been loved 0 times :('
    else:
      return 'I have been loved {0} time{1}:\n{2}'.format(nLoves, 's' if nLoves != 1 else '', ret)
