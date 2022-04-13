import csv
import re 

class Pre_process():
  def __init__(self, path ):
    self.path = path
    self.all_song = []
    self.type_ = 'r'
    self.encoder = 'utf-8'

  def Clean(self):
    with open(self.path,self.type_, encoding=self.encoder ) as file :
      line = csv.reader(file, delimiter ='\n')
      separating = ''.join(re.sub( r"([A-Z])", r", \1", line[0]))
        remo_comma = re.sub(r"(^,)","",separating)
        self.all_song.append(''.join(re.sub(r"(^ )","",remo_comma)))
        output  = ' '.join(line for line in all_song)
    return output
