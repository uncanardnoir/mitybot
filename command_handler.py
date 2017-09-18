from collections import namedtuple
from handlers import whoareyou
from handlers import soupoftheday
from handlers import arbitrarynumber
from handlers import randomnumber
from handlers import hello
from handlers import memehandler

class CommandHandler():
  def __init__(self):
    # Commands that have a description will be public. Ones that don't will be hidden
    memeHandler = memehandler.MemeHandler()
    self.commands = {
      'whoareyou': ( whoareyou.Whoareyou(), "prints information about Mitybot 2.0" ),
      'soupoftheday': ( soupoftheday.Soupoftheday(), "gets the soup of the day" ),
      'arbitrarynumber': ( arbitrarynumber.Arbitrarynumber(), "returns an arbitrary number" ),
      'randomnumber': ( randomnumber.Randomnumber(), None ),
      'hello': ( hello.Hello(), "say hello to Mitybot!" ),
      'mock': ( memeHandler, None ),
      'success': ( memeHandler, None ),
      'notsureif': ( memeHandler, None ),
      'feelsbad': ( memeHandler, None )
    }
    self.Command = namedtuple('Command', 'command args parent')

  def handleCommand(self, result, command):
    # dispatcher
    args = command.split(' ', 1)
    command = args[0]
    args = args[1:]
    if command.lower() in self.commands:
      handler = self.commands[command.lower()][0]
      command = self.Command(command, args, result)
      return handler.handleCommand(command)
    return None
