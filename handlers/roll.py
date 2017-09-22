import random
from array import array

class Roll():
  def __init__(self):
    #warning, not true randomness
    random.seed()
    
  def handleCommand(self, command):
    try:
      dice = self.parseRequest(command.args)
      result = self.rollDice(dice)
      return self.resultToString(result)
    except:
      return "Those aren't dice!"
      
  def parseRequest(self, command):
    #parses the dice request into a tuple of the form {numDice, Type}
    dice = command.split("d")
    if len(dice) != 2:
      raise ValueError('Wrong Number of arguements')
    return dice
    
  def rollDice(self, dice):
    #rolls the dice and returns an array of the dice values
    rolls = array('i')
    if len(dice) != 2:
      raise ValueError('Wrong Number of arguements')
    for i in range(int(dice[0])):
      rolls.append(random.randint(1,int(dice[1])))
    return rolls
  
  def resultToString(self, rolls):
    total = 0
    result = ""
    for i in rolls:
      result = result + str(i) + ', '
      total = total + i
    result = result + "Total: " + str(total)
    return result
    
