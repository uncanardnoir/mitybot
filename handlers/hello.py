from jsonpath_rw import jsonpath, parse

class Hello():
  def handleCommand(self, command):
    name = parse('$.message.from.first_name').find(command.parent)
    if name:
      return 'Herro {0}!'.format(name[0].value)
