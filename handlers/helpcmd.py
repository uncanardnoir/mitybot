class HelpCmd():
  def setCommands(self, obj):
    self.obj = obj

  def handleCommand(self, command):
    ret = ''
    for key in self.obj:
      if self.obj[key][1]:
        ret += ('/mitybot ' + key + ' - ' + self.obj[key][1] + '\n')
    return ret
