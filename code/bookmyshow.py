import requests
from bs4 import BeautifulSoup
import os.path
import pprint
import re
#os.chdir('bookmyshow')
# url = 'http://in.bookmyshow.com/hyderabad/movies'
r = requests.get('http://in.bookmyshow.com/hyderabad/movies').text
d = BeautifulSoup(r,"html.parser")
extract = d.findAll("a", "__movie-name").__str__()
sim = re.split(r'</a>', extract)
# s = str(extract)
# file = open("buff/ap.txt","w")
# file.write(s)
matching = [s for s in sim if "data-id" in s]
print type(matching)

pprint.pprint(a)