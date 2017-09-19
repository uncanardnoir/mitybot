import random

class DickPic:
  def __init__(self):
    self.dicks = ['https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/46_Dick_Cheney_3x4.jpg/220px-46_Dick_Cheney_3x4.jpg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Secretary_of_Defense_Richard_B._Cheney%2C_official_portrait.jpg/170px-Secretary_of_Defense_Richard_B._Cheney%2C_official_portrait.jpg',
'https://theredshtick.com/wp-content/uploads/2014/06/dick_cheney-asshole.jpg',
'https://www.newyorker.com/wp-content/uploads/2014/12/borowitz-dick-cheney-mtp-1200.jpg',
'http://i.telegraph.co.uk/multimedia/archive/01242/cheney_1242441c.jpg',
'http://static4.businessinsider.com/image/55088bc8ecad0497094416fe/dick-cheney-just-gave-an-emotional-and-intense-interview-in-playboy.jpg',
'http://prn.fm/wp-content/uploads/2015/07/dick-cheney.jpg',
'http://a.abcnews.com/images/Politics/GTY_dick_cheney_jt_160918_4x3_992.jpg',
'https://www.thefamouspeople.com/profiles/images/dick-cheney-6.jpg']

  def handleCommand(self, command):
    return ('imageLink', self.dicks[random.randrange(len(self.dicks))]) 
