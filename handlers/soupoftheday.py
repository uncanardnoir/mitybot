from datetime import datetime
import pytz

class Soupoftheday():
  def __init__(self):
    self.soups = ['Gazpacho', 'Tomato Bisque', 'Cheddar', 'French Onion', 'Split Pea', 'Leek', 'Dog', 'Beef Noodle', 'Clam Chowder', 'Carrot', 'Minestrone', 'Coconut', 'Chicken Noodle', 'Autumn Squash', 'Cream of Chicken and Rice', 'Broccoli Cheddar', 'Turkey Chili', 'Baked Potato', 'Poop', 'Lentil', 'Garbanzo Bean']

  def handleCommand(self, command):
    date = datetime.now(pytz.timezone('America/New_York')).date()
    idx = hash(date) % len(self.soups)
    return 'The soup of the day is: {0}'.format(self.soups[idx])
