#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
import codecs
import pdb
import sqlite3

db=sqlite3.connect("elec.db")

c=db.cursor()
res=c.execute("select name, url from OIKS;")
for r in res:
    print(f"Скачиваем данные для {r[0]}")
db.close()


