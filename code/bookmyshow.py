import requests
from bs4 import BeautifulSoup
import os.path
import pprint
import re
# os.chdir('bookmyshow')
# url = 'http://in.bookmyshow.com/hyderabad/movies'
r = requests.get('http://in.bookmyshow.com/hyderabad/movies').text
d = BeautifulSoup(r,"html.parser")
extract = d.findAll("a", "__movie-name").__str__()
sim = re.split(r'</a>', extract)
matching = [s for s in sim if "data-id" in s]
# ### getting URL
paturl = re.compile(r'href="+.*\"\s')
# url = re.split(r'"', (re.findall(paturl, matching[1]))[0])[1]
# ### getting title
pattit = re.compile(r'title="+.*"')
# title = re.split(r'"',(re.findall(pattit,matching[1]))[0])[1]

tidict = {}
for i in xrange(len(matching)):
    title = re.split(r'"', (re.findall(pattit, matching[i]))[0])[1]
    url = re.split(r'"', (re.findall(paturl, matching[i]))[0])[1]
    tidict.update({title: url})
print type(tidict)
# finding your film name
a = [value for key, value in tidict.items() if 'spec' in key.lower()]
print a
