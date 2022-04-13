import re
import csv
import time
import requests
from bs4 import BeautifulSoup

class Crawler_Canserbero (object):
    def __init__(self,url):
        self.url = url
        self.links = []
        self.all_song = []
        
        
    def _Main_Website (self, Ourl = None , Outer = False):

        if Outer:
            website = requests.get(Ourl)
        else:
            website = requests.get(self.url)
        bs = BeautifulSoup(website.content, "html.parser")
        return bs 
        
    def _extract_all_links (self):
    
        bs = self._Main_Website()
        # -----> exrtract all the links 
        for letter in bs.find_all("div",attrs = {'class':'list-container'}):
            for song in letter.find_all("a", attrs = {'class':'song-name'},href=True):
                self.links.append(str("http://letras.com")+song['href'])

    def _song_by_song (self):
        bs = self._extract_all_links() 
        
        file = open("Canserbero_songs.txt", "w" , encoding="utf-8") 

        for song_url in self.links:
            bs = self._Main_Website(Ourl =song_url , Outer =True)
            for row in bs.select("#js-lyric-cnt > article > div.cnt-letra-trad.g-pr.g-sp > div.cnt-letra.p402_premium > p"):
                file.write(row.get_text(separator = "\n")) 
                self.all_song.append(row.get_text(separator = " "))
        print("done")
        file.close() 
