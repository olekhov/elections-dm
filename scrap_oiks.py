#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
import codecs
import pdb
import sqlite3

db=sqlite3.connect("elec.db")

with codecs.open("mgik.html",encoding="windows-1251") as f:
    mgikh=f.read()

s=BeautifulSoup(mgikh)
c=db.cursor()
c.execute("delete from OIKS;")
for x in s.find('select'):
    print(f"{x.text}: [{x.get('value')}]")
    if x.get('value')!=None:
        c.execute(f"INSERT INTO OIKS VALUES ('{x.text}','{x.get('value')}');")
db.commit()
db.close()


