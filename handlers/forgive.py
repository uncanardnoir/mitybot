import os
from jsonpath_rw import jsonpath, parse

class Forgive():
  def handleCommand(self, command):
    if command.command.lower() == "getforgives":
      return self.getForgiveString()
    userId = parse('$.message.from.id').find(command.parent)
    if not userId:
      return None
    userId = userId[0].value
    if not userId == 313082320: #Ryan's id
      return "Pshhh. You cannot forgive strikes."
    if command.command.lower() == "forgive":
      strikeUser = command.args.lower()
      if not strikeUser:
        return None
      return self.forgiveUser(strikeUser)
    return None
      
  def forgiveUser(strikeUser):
    userStrikeFile = 'strike/{0}'.format(strikeUser)
    userForgiveFile = 'forgive/{0}'.format(strikeUser)
    if not os.path.isfile(userStrikeFile):
      return "Nothing to forgive."
    else:
      nStrikes = 0
      nForgives = 0
      with open(userStrikeFile, "r+") as f:
        data = f.read().split()
        nStrikes = int(data[1])
        f.seek(0)
        f.write("{0}\n0".format(strikeUser))
        f.truncate()
      with open(userForgiveFile, "r+") as f:
        data = f.read().split()
        if not data:
          nForgives = nStrikes
        else:
          nForgives = int(data[1]) + nStrikes
        f.seek(0)
        f.write("{0}\n{1}".format(strikeUser, nForgives))
        f.truncate()
      return "{0}, your corndad has forgiven you. You have been saved {1} strikes for a total of {2} strikes.".format(strikeUser, nStrikes, nForgives)

  def getForgiveString(self):
    ret = ''
    nStrikes = 0
    for filepath in os.listdir('forgive'):
      with open(os.path.join('forgive', filepath), "r") as f:
        data = f.read().split()
        thisForgive = int(data[1])
        thisName = data[0]
        thisline = '{0}: {1} forgive{2}\n'.format(thisName, thisForgive, 's' if thisForgive != 1 else '')
        ret += thisline
        nStrikes = nStrikes + thisForgive
    if nStrikes == 0:
      return 'There are no strikes!'
    else:
      return 'Current forgive records:\n{0}'.format(ret)