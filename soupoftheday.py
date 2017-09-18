import datetime

class Soupoftheday():
  def __init__(self):
    self.soups = ['Gazpacho', 'Tomato Bisque', 'Cheddar', 'French Onion', 'Pea', 'Leek', 'Dog', 'Beef Noodle', 'Clam Chowder', 'Carrot', 'Minestrone', 'Coconut', 'Chicken Noodle', 'Autumn Squash', 'Cream of Chicken and Rice', 'Broccoli Cheddar', 'Turkey Chili', 'Baked Potato', 'Poop']

  def handleCommand(self, args):
    date = datetime.date.today()
    idx = hash(date) % len(self.soups)
    return 'The soup of the day is: {0}'.format(self.soups[idx])
