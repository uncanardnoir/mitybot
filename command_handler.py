from whoareyou import Whoareyou
from soupoftheday import Soupoftheday
from arbitrarynumber import Arbitrarynumber
from randomnumber import Randomnumber

class CommandHandler():
  def __init__(self):
    # Commands that have a description will be public. Ones that don't will be hidden
    self.commands = {
      'whoareyou': ( Whoareyou(), "prints information about Mitybot 2.0" ),
      'soupoftheday': ( Soupoftheday(), "gets the soup of the day" ),
      'arbitrarynumber': ( Arbitrarynumber(), "returns an arbitrary number" ),
      'randomnumber': ( Randomnumber(), None )
    }

  def handleCommand(self, result, command):
    # dispatcher
    args = command.split(' ', 1)
    command = args[0]
    args = args[1:]
    if command.lower() in self.commands:
      handler = self.commands[command.lower()][0]
      return handler.handleCommand(args)
    return None
