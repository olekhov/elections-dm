#!/usr/bin/env python3.7

# Скачивание информации об Окружных избирательных комиссиях (45 округов в Москве)

from bs4 import BeautifulSoup
import codecs
import pdb
import sqlite3
import requests

db=sqlite3.connect("elec.db")
r=requests.Session()
r.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
# МГИК
u='http://www.moscow_city.vybory.izbirkom.ru/region/moscow_city?action=show&vrn=27720002327736&region=77&prver=0&pronetvd=null'
mgikh=r.get(u,headers={"referer":"http://www.moscow_city.vybory.izbirkom.ru/region/moscow_city"})

s=BeautifulSoup(mgikh.text, "html.parser")
#pdb.set_trace()
c=db.cursor()
c.execute("delete from OIKS;")
for x in s.find('select'):
    print(f"{x.text}: [{x.get('value')}]")
    if x.get('value')!=None:
        c.execute(f"INSERT INTO OIKS(oik_name,url) VALUES ('{x.text}','{x.get('value')}');")
db.commit()
db.close()


