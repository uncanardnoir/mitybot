from collections import namedtuple
from handlers import whoareyou
from handlers import soupoftheday
from handlers import arbitrarynumber
from handlers import randomnumber
from handlers import hello
from handlers import memehandler
from handlers import currenttime
from handlers import helpcmd
from handlers import dickpic
from handlers import iloveyou
from handlers import magic8ball
from handlers import questions
from handlers import badbot
from handlers import strike
from handlers import forgive
from handlers import hotdognothotdog
from handlers import roll
from handlers import supposably
from handlers import tellajoke

class CommandHandler():
  def __init__(self):
    # Commands that have a description will be public. Ones that don't will be hidden
    memeHandler = memehandler.MemeHandler()
    badbotHandler = badbot.BadBot()
    strikeHandler = strike.Strike()
    forgiveHandler = forgive.Forgive()
    self.commands = {
      'whoareyou': ( whoareyou.Whoareyou(), "prints information about Mitybot 2.0" ),
      'soupoftheday': ( soupoftheday.Soupoftheday(), "gets the soup of the day" ),
      'arbitrarynumber': ( arbitrarynumber.Arbitrarynumber(), "returns an arbitrary number" ),
      'randomnumber': ( randomnumber.Randomnumber(), None ),
      'hello': ( hello.Hello(), "say hello to Mitybot!" ),
      'supposably': ( supposably.Supposably(), None ),
      'mock': ( memeHandler, None ),
      'success': ( memeHandler, None ),
      'notsureif': ( memeHandler, None ),
      'feelsbad': ( memeHandler, None ),
      'currenttime': ( currenttime.CurrentTime(), "gets the current time" ),
      'help': ( helpcmd.HelpCmd(), "prints help" ),
      'dickpic': ( dickpic.DickPic(), "gets a dick pic"),
      'iloveyou': ( iloveyou.ILoveYou(), None ),
      'magic8ball': ( magic8ball.Magic8Ball(), None ),
      'question': ( questions.Question(), "answers your questions"),
      'badbot': ( badbotHandler, None ),
      'goodbot': ( badbotHandler, None ),
      'strike': ( strikeHandler, None),
      'deletestrikes': ( strikeHandler, None),
      'getstrikes': ( strikeHandler, "prints the current strike count"),
      'hotdognothotdog': ( hotdognothotdog.HotdogNotHotdog(), "It's a hotdog ... or not a hotdog"),
      'roll': (roll.Roll(), "rolls dice, use XdY format"),
      'forgive': ( forgiveHandler, None),
      'getforgives': ( forgiveHandler, "prints the current forgive count"),
      'tellajoke': ( tellajoke.TellAJoke(), "tell a joke" )
    }
    self.commands['help'][0].setCommands(self.commands)
    self.commands['whoareyou'][0].setLover(self.commands['iloveyou'][0])
    self.Command = namedtuple('Command', 'command args parent')

  def handleCommand(self, result, command):
    # dispatcher
    args = command.split(' ', 1)
    command = args[0]
    args = args[1:]
    if command.lower() in self.commands:
      handler = self.commands[command.lower()][0]
      command = self.Command(command, args[0] if args else None, result)
      return handler.handleCommand(command)
    return None
