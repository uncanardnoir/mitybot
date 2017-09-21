class BadBot():
  def handleCommand(self, command):
    with open('badbotcounter/counter', 'r+') as f:
      count = int(f.read())
      if command.command == "badbot":
        count = count - 1
        ret = ":(\n[Score: {0}]".format(count)
      if command.command == "goodbot":
        count = count + 1
        ret = ":)\n[Score: {0}]".format(count)
      f.seek(0)
      f.write(str(count))
      f.truncate()
      return ret
