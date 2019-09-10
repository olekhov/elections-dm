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
c.execute("delete from UIK_Protocol;")
c.execute("select u.uik_name, u.url, u.ID from UIKS u;")
for u in c.fetchall():
    uik_num=int(u[0].split(' ')[0])
    uik_id = u[2]
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

    protobs=BeautifulSoup(proto_text,"html.parser")
    main_table=protobs.find_all("table")[-2]
    rows=main_table.find_all("tr")

    line_order=1
    for r in rows:
        data=r.find_all("td")
        #pdb.set_trace()
        line_num=data[0].text
        if line_num == "" :
            continue
        line_name=data[1].text
        line_value=int(data[2].text)
        candidate_id=-1
        if line_order>12 :
            c.execute(f"SELECT c.ID from Candidates c WHERE c.candidate_name='{line_name}';")
            res=c.fetchone()
            if res == None:
                print(f"Кандидат {line_name} не найден!")
            else:
                candidate_id=res[0]
            pass
        #pdb.set_trace()

        q=f"""INSERT INTO UIK_Protocol(
            uik_id,row_number,row_name,row_value,row_order,candidate_id) VALUES
            ({uik_id},'{line_num}','{line_name}',{line_value},{line_order},{candidate_id});
            """
        c.execute(q)
        line_order = line_order+1

        pass

    pass


db.commit()
db.close()


