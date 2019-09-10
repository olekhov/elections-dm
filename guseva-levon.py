#!/usr/bin/env python3.7

import numpy as np
import matplotlib.pyplot as plt
import csv
import pdb
import sqlite3

db=sqlite3.connect("elec.db")
q=f"""SELECT u.uik_name, p_guseva.row_value,p_smirnov.row_value, p_smirnov.row_value>p_guseva.row_value
FROM UIKS u, UIK_Protocol p_guseva, UIK_Protocol p_smirnov, Candidates guseva, Candidates smirnov
WHERE
p_guseva.uik_id = u.id AND
p_smirnov.uik_id = u.id AND
guseva.candidate_name like 'Гусева %' AND
smirnov.candidate_name like 'Смирнов %' AND
p_guseva.candidate_id = guseva.id AND
p_smirnov.candidate_id = smirnov.id
ORDER BY 4,3"""
c=db.cursor()
c.execute(q)
data = c.fetchall()
#pdb.set_trace()

group_names  =  list([ ' '.join(x[0].split(' ')[1:3]) for x in data])
group_guseva =  list([int(x[1]) for x in data])
group_smirnov = list([int(x[2]) for x in data])
group_win = list([(600 if x[3] else 0) for x in data])
#pdb.set_trace()

#plt.rcdefaults()
fig,ax_w=plt.subplots(figsize=(6,20),dpi=150)
ax_g = ax_w.twiny()
ax_l = ax_w.twiny()
ax_w.set_xlim(xmin=0,xmax=600)
#ax_w.set_visible(False)
ax_w.barh(group_names, group_win, color=(0.8,1.0,0.8))

ax_g.set_xlim(xmin=0,xmax=600)
ax_g.barh(group_names, group_guseva, height=0.7, label = "Гусева", color=(0.8,0.8,0.8))
ax_g.xaxis.tick_bottom()

ax_l.set_xlim(xmin=600,xmax=0)
ax_l.barh(group_names, group_smirnov, height=0.7, label = "Левон", color=(1,0,0))
ax_l.xaxis.tick_top()


#ax.set_xlim(xmin=0,xmax=6000)
#ax.barh(group_names, group_signs)
#plt.bar(group_, group_signs, width=1)

ax_l.legend(loc=1)
ax_g.legend(loc=2)
#plt.show()

fig.savefig("guseva-levon.png",dpi=150, bbox_inches="tight")
