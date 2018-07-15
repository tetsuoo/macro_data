import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("final_of_final.csv")

a = pd.read_csv("oecd_countries.csv")
oecd = a.countrycode

###GRAPHICS


fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()

ax = fig1.add_subplot(4,3,1)
ax.plot([], [], label="GDP per Capita")
ax.plot([], [], '--b', label="Share of Gross Capital Formation")
ax.plot([], [], '0.5', label='Share of FDI over GDP')
ax.patch.set_visible(False)
ax.axis('off')
ax.legend(loc='center', frameon=False)

def income_graph():
    for i in range(len(oecd)):
        X = df.loc[df['countrycode']==oecd[i]].year
        Y = df.loc[df['countrycode']==oecd[i]].ave_income
        Z = df.loc[df['countrycode']==oecd[i]].csh_i
        W = df.loc[df['countrycode']==oecd[i]].fdi
        if (i <= 10):
            ax = fig1.add_subplot(4,3,i+2)
        elif (i >= 11) and (i <= 22):
            ax = fig2.add_subplot(4,3,i-10)
        else:
            ax = fig3.add_subplot(4,3,i-22)

        ax.plot(X, Y, label="GDP per Capita")
        ax.plot(X, Z, '--b', label="Share of Gross Capital Formation")
        ax.plot(X, W, '0.5', label='Share of Net FDI Inflow over GDP')
        ax.text(0.1,0.8,oecd[i],
            horizontalalignment='center',
            transform=ax.transAxes,
            fontsize=18)
    plt.show()

income_graph()
