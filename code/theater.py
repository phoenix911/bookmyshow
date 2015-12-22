import requests
from bs4 import BeautifulSoup
import re
from pydub import AudioSegment
from pydub.playback import play
import time
import os.path
print os.getcwd()

#r = requests.get(').text

song = AudioSegment.from_ogg("starwars.ogg")


def notification(url):
    r = requests.get(url).text
    d = BeautifulSoup(r,"html.parser")
    extract = d.findAll("div", "date-container").__str__()
    da = re.findall(r'\D(\d{2})\D',extract)
    print da
    if '25' in da:
        play(song)
    else:
        print 'hello'
    time.sleep(60)

# url = 'http://in.bookmyshow.com/buytickets/in-the-heart-of-the-sea-3d-hyderabad/movie-hyd-ET00036260-MT/20151222'
url = 'http://in.bookmyshow.com/buytickets/star-wars-the-force-awakens-3d-hyderabad/movie-hyd-ET00025699-MT/20151224'

while True:
    notification(url)

