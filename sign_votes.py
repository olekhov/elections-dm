#!/usr/bin/env python3.7

import numpy as np
import matplotlib.pyplot as plt
import csv
import pdb

data={}
num=1
with open("sign_votes_data.txt","r") as f:
    reader=csv.reader(f, delimiter='\t')
    for row in reader:
        data[row[0]] = { 'votes' : int(row[1]), 'signs': int(row[2]) }
        num=num+1
        if num>=20:
            break


group_names=list(data.keys())
group_votes=list([x['votes'] for x in data.values()])
group_signs=list([x['signs'] for x in data.values()])
#pdb.set_trace()

#plt.rcdefaults()
fig,ax=plt.subplots(figsize=(6,10))
ax.barh(group_names, group_signs, label = "Подписи (3% от списка)")
ax.barh(group_names, group_votes, 0.25, color=(1,0,0), label="Голоса")
#ax.set_xlim(xmin=0,xmax=6000)
ticks=(0,1000,2000,3000,4000,5000)
ax.set_xticks(ticks,ticks )
#ax.barh(group_names, group_signs)
#plt.bar(group_, group_signs, width=1)

ax.legend(ncol=2)
#plt.show()

fig.savefig("sign_votes.png",dpi=150, bbox_inches="tight")
