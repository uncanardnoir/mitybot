import random

class DickPic:
  def __init__(self):
#    self.dicks = ['https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/46_Dick_Cheney_3x4.jpg/220px-46_Dick_Cheney_3x4.jpg',
#'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Secretary_of_Defense_Richard_B._Cheney%2C_official_portrait.jpg/170px-Secretary_of_Defense_Richard_B._Cheney%2C_official_portrait.jpg',
#'https://theredshtick.com/wp-content/uploads/2014/06/dick_cheney-asshole.jpg',
#'https://www.newyorker.com/wp-content/uploads/2014/12/borowitz-dick-cheney-mtp-1200.jpg',
#'http://i.telegraph.co.uk/multimedia/archive/01242/cheney_1242441c.jpg',
#'http://static4.businessinsider.com/image/55088bc8ecad0497094416fe/dick-cheney-just-gave-an-emotional-and-intense-interview-in-playboy.jpg',
#'http://prn.fm/wp-content/uploads/2015/07/dick-cheney.jpg',
#'http://a.abcnews.com/images/Politics/GTY_dick_cheney_jt_160918_4x3_992.jpg',
#'https://www.thefamouspeople.com/profiles/images/dick-cheney-6.jpg']
    self.dicks = ['https://1.bp.blogspot.com/_TVfEjAyW4Fk/R2CEYHBjl4I/AAAAAAAAEfM/hsUPs6poZCo/s400/Mr.+D.jpg',
    'http://bp2.blogger.com/_TVfEjAyW4Fk/R2CEiXBjl7I/AAAAAAAAEfk/H5dWFiVQs-U/s1600-h/DeclorationofInDpenis.png',
    'http://bp1.blogger.com/_TVfEjAyW4Fk/R2CEbHBjl5I/AAAAAAAAEfU/5fSw_RcU79s/s1600-h/magicP.jpg',
    'http://bp0.blogger.com/_TVfEjAyW4Fk/R2CEQ3Bjl2I/AAAAAAAAEe8/-v2yxp3Qtm8/s1600-h/titandick.jpg',
    'http://bp3.blogger.com/_TVfEjAyW4Fk/R2CEnnBjl8I/AAAAAAAAEfs/qZf6mZkE1_o/s1600-h/choochooP.jpg',
    'http://i.imgur.com/HILtLOi.png',
    'https://i.ytimg.com/vi/DoTN51V25Rw/hqdefault.jpg',
    'https://i.ytimg.com/vi/UOEN3KC-UAc/hqdefault.jpg',
    'https://thespewblog.files.wordpress.com/2015/06/banana_penis.jpg']

  def handleCommand(self, command):
    return ('imageLink', self.dicks[random.randrange(len(self.dicks))]) 
