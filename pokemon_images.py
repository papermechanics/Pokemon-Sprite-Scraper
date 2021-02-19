import requests as rq
from bs4 import BeautifulSoup as bsoup
import pandas as pd
from time import sleep
from random import randint

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
img_srcs = []
names = []
page = rq.get( 'https://pokemondb.net/pokedex/national', headers = headers)
soup = bsoup( page.content , 'html.parser')
pokeimg_containers = soup.find_all( 'span' , class_ = 'infocard-lg-img' )
for each in pokeimg_containers:
    name = each.a.span['data-src']
    img_srcs.append(name)
pokename_containers = soup.find_all('a', class_ = 'ent-name' )
for each in pokename_containers:
    name = each.string.lower()
    names.append(name)
for i in range(0,151): #modify to required pokedex entry
    url = img_srcs[i]
    r = rq.get(url)
    with open('C://Users/lenovo/Desktop/pokemon images/images/{}.png'.format(names[i]) , 'wb') as f: #replace with your location
        f.write(r.content)
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    sleep(1)