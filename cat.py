class Util():
  def __init__(self, files):
    self.files = files
  def run(self):
    for file in self.files:
      with open(file) as f:
        for line in f:
          print line,
def show():
  print """
 /\     /\\
{  `---'  }
{  O   O  }
~~>  V  <~~
 \  \|/  /
  `-----'__
  /     \  `^\_
 {       }\ |\_\_   W
 |  \_/  |/ /  \_\_( )
  \__/  /(_E     \__/
    (  /
     MM
     """
