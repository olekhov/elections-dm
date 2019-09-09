#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
import codecs
import pdb
import sqlite3
import requests

# Скачивание информации о Кандидатах

db=sqlite3.connect("elec.db")
url="http://www.moscow_city.vybory.izbirkom.ru/region/region/moscow_city?action=show&root=772000140&tvd=27720002327880&vrn=27720002327736&region=77&global=&sub_region=77&prver=0&pronetvd=null&vibid=27720002327736&type=220"

r=requests.Session()
r.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
post_data={
        "search_surname": "",
        "search_name":"",
        "search_secondname":"",
        "search_party":"",
        "search_okrug":"",
        "search_vidvig":"",
        "search_registr":"", # "зарегистрирован"
        "search_izbr":"",
        "vrnio":"",
        "rep_action":"search"}

candh=r.post(url, data=post_data)
pdb.set_trace()
while candh.status_code !=200:
    print("Ошибочка, скачиваем ещё разок")
    candh=r.get(url)
bs=BeautifulSoup(candh.text,"html.parser")
t=bs.find('table', attrs={"id":"table-2"})

c=db.cursor()

for r in t.find('tbody').find_all('tr'):
    td = r.find_all('td')
    if td[-2].text == 'зарегистрирован':
        print(f"РЕГ: {td[1].text} Округ {td[4].text}")
        party=c.execute(f"SELECT id FROM Parties WHERE party_name='{td[3].text}';")
        if party==None:
            print(f"Нет такой партии: {td[3]}")
            c.execute(f"INSERT INTO Parties(party_name) VALUES('{td[3]}');")
        c.execute("INSERT INTO Candidates(candidate_name,



