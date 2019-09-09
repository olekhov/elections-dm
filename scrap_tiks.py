#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
import codecs
import pdb
import sqlite3
import requests

# Скачивание информации о Территориальных избирательных комиссиях

db=sqlite3.connect("elec.db")

mgik_top="http://www.moscow_city.vybory.izbirkom.ru/region/moscow_city?action=show&vrn=27720002327736&region=77&prver=0&pronetvd=null"
r=requests.Session()
r.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
c=db.cursor()
c.execute("delete from TIKS;")
c.execute("select oik_name, url, ID from OIKS;")
for t in c.fetchall():
    print(f"Скачиваем данные для {t[0]}")
    #pdb.set_trace()
    tikh=r.get(t[1],headers={"referer":mgik_top})
    while tikh.status_code !=200:
        print("Ошибочка, скачиваем ещё разок")
        tikh=r.get(t[1],headers={"referer":mgik_top})
    bs=BeautifulSoup(tikh.text,"html.parser")
    print(f"В этом ОИК такие ТИКи:")
    for tik in bs.find('select'):
        print(f"{tik.text}")
        if tik.get('value')!=None:
            c.execute(f"INSERT INTO TIKS(oik,tik_name,url) VALUES ({t[2]},'{tik.text}','{tik.get('value')}');")
db.commit()
db.close()


