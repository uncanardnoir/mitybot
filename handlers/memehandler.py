import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def makememe(topString, bottomString, filename):
  if not topString:
    topString = " "

  if not bottomString:
    bottomString = " "
 
  img = Image.open(filename)
  imageSize = img.size
  fontSize = int(imageSize[1]/5)
  font = ImageFont.truetype('impact.ttf', fontSize)
  topTextSize = font.getsize(topString)
  bottomTextSize = font.getsize(bottomString)
  while topTextSize[0] > imageSize[0]-20 or bottomTextSize[0] > imageSize[0]-20:
    fontSize = fontSize - 1
    font = ImageFont.truetype('impact.ttf', fontSize)
    topTextSize = font.getsize(topString)
    bottomTextSize = font.getsize(bottomString)

  # find top centered position for top text
  topTextPositionX = (imageSize[0]/2) - (topTextSize[0]/2)
  topTextPositionY = 0
  topTextPosition = (topTextPositionX, topTextPositionY)

  # find bottom centered position for bottom text
  bottomTextPositionX = (imageSize[0]/2) - (bottomTextSize[0]/2)
  bottomTextPositionY = imageSize[1] - bottomTextSize[1]
  bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

  draw = ImageDraw.Draw(img)

  # draw outlines
  # there may be a better way
  outlineRange = int(fontSize/15)
  for x in range(-outlineRange, outlineRange+1):
    for y in range(-outlineRange, outlineRange+1):
      draw.text((topTextPosition[0]+x, topTextPosition[1]+y), topString, (0,0,0), font=font)
      draw.text((bottomTextPosition[0]+x, bottomTextPosition[1]+y), bottomString, (0,0,0), font=font)

  draw.text(topTextPosition, topString, (255,255,255), font=font)
  draw.text(bottomTextPosition, bottomString, (255,255,255), font=font)

  return img

def splithalf(text):
  i = int(len(text)/2)
  while i > 0 and text[i] != ' ':
    i = i - 1
  return (text[:i], text[i:])

def stupefy(text):
  result = []
  for i in range(len(text)):
    result.append(text[i].lower() if i % 2 == 0 else text[i].upper())
  return "".join(result)

class MemeHandler():
  def __init__(self):
    self.normiememes = {
      "mock": "memes/mocking-spongebob.jpg",
      "success": "memes/success.jpg",
      "notsureif": "memes/notsureif.jpg",
      "feelsbad": "memes/feelsbadman.jpg"
    }

  def handleCommand(self, command):
    if not command.command.lower() in self.normiememes:
      return
    filename = self.normiememes[command.command.lower()]
    if command.command == "mock":
      memeText = stupefy(command.args[0])
    else:
      memeText = command.args[0]
    if len(memeText) > 75:
      split = ("Index out of range exception in", "doSendRequest(text, cred={\"user\": \"mity\", \"pass\": \"iloveryan\"})")
    else:
      split = splithalf(memeText)
    return makememe(split[0], split[1], filename)
