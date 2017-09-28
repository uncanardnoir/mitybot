import os
from jsonpath_rw import jsonpath, parse

class Strike():
  def handleCommand(self, command):
    if command.command.lower() == "getstrikes":
      return self.getStrikesString()
    userId = parse('$.message.from.id').find(command.parent)
    if not userId:
      return None
    userId = userId[0].value
    if not userId == 313082320: #Ryan's id
      if command.command.lower() == "deletestrikes":
        return "Pshhh. You cannot delete strikes."
      else:
        return "Pshhh. You cannot assign strikes." 
    if command.command.lower() == "deletestrikes":
      return self.deleteStrikes()
    if not command.args:
      return None
    strikeUser = command.args.lower()
    userFile = 'strike/{0}'.format(strikeUser)
    if not os.path.isfile(userFile):
      with open(userFile, "w") as f:
        f.write("{0}\n1".format(strikeUser))
        nStrikes = 1
    else:
      with open(userFile, "r+") as f:
        data = f.read().split()
        nStrikes = int(data[1]) + 1
        f.seek(0)
        f.write("{0}\n{1}".format(strikeUser, nStrikes))
        f.truncate()
    return "Careful {0}. You are now at {1} strike{2}.".format(strikeUser, nStrikes, 's' if nStrikes != 1 else '')

  def getStrikesString(self):
    ret = ''
    nStrikes = 0
    for filepath in os.listdir('strike'):
      with open(os.path.join('strike', filepath), "r") as f:
        data = f.read().split()
        thisStrike = int(data[1])
        thisName = data[0]
        thisline = '{0}: {1} strike{2}\n'.format(thisName, thisStrike, 's' if thisStrike != 1 else '')
        ret += thisline
        nStrikes = nStrikes + thisStrike
    if nStrikes == 0:
      return 'There are no strikes!'
    else:
      return 'Current strike records:\n{0}'.format(ret)
	  
  def deleteStrikes(self):
    for filepath in os.listdir('strike'):
      os.remove(os.path.join('strike', filepath))
