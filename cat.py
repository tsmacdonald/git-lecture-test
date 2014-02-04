class Util():
  def __init__(self, files):
    self.files = files
  def run(self):
    for file in self.files:
      with open(file) as f:
        for line in f:
          print line,

class FriendlyCat():
  def __init__(self, friend_name):
    self.friend = friend_name

  def show(self):
    print """
 /\     /\\
{  `---'  }
{  O   O  }
~~>  V  <~~   Hello, %s
 \  \|/  /
  `-----'__
  /     \  `^\_
 {       }\ |\_\_   W
 |  \_/  |/ /  \_\_( )
  \__/  /(_E     \__/
    (  /
     MM
     """%self.friend
