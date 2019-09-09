#!/usr/bin/env python3.7

# Скачивание информации об Участковых избирательных комиссиях

from bs4 import BeautifulSoup
import codecs
import pdb
import sqlite3
import requests


db=sqlite3.connect("elec.db")

r=requests.Session()
r.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
c=db.cursor()
c.execute("delete from UIKS;")
c.execute("select t.tik_name, t.url, t.ID from TIKS t;")
for t in c.fetchall():
    print(f"Скачиваем данные для {t[0]}")
    #pdb.set_trace()
    tikh=r.get(t[1])
    while tikh.status_code !=200:
        print("Ошибочка, скачиваем ещё разок")
        tikh=r.get(t[1])
    bs=BeautifulSoup(tikh.text,"html.parser")
    print(f"В этом ТИК такие УИКи:")
    for uik in bs.find('select'):
        print(f"{uik.text}")
        if uik.get('value')!=None:
            c.execute(f"INSERT INTO UIKS(tik,uik_name,url) VALUES ({t[2]},'{uik.text}','{uik.get('value')}');")
db.commit()
db.close()


