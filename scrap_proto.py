#!/usr/bin/env python3.7

# Скачивание информации из протоколов отдельных Участковых избирательных комиссиях

from bs4 import BeautifulSoup
import codecs
import pdb
import sqlite3
import requests
from pathlib import Path


db=sqlite3.connect("elec.db")

r=requests.Session()
r.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
r.keep_alive = False
c=db.cursor()
#c.execute("delete from UIK_Protocol;")
c.execute("select u.uik_name, u.url from UIKS u;")
for u in c.fetchall():
    uik_num=int(u[0].split(' ')[0])
    print(f"Скачиваем данные для УИК {uik_num}")
    #pdb.set_trace()
    proto_file=f"cached-proto/{uik_num:04}.html"
    if Path(proto_file).is_file():
        print(f"Протокол уже скачан")
        with open(proto_file,"r") as f:
            proto_text=f.read()
    else:
        uikh=r.get(u[1])
        while uikh.status_code !=200:
            print("Ошибочка, скачиваем ещё разок")
            uikh=r.get(u[1])
        bs=BeautifulSoup(uikh.text,"html.parser")
        proto_url=bs.select('td',attrs={"class":"tdReport"})[-1].select('a')[0].get('href')

        protoh=r.get(proto_url)
        while protoh.status_code !=200:
            print("Ошибочка, скачиваем ещё разок")
            protoh=r.get(proto_url)

        proto_text=protoh.text

        with open(proto_file,"w") as f:
            f.write(proto_text)
        print(f"Протокол не был скачан, скачали.")

    #pdb.set_trace()

db.commit()
db.close()


