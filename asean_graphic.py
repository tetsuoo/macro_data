import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("asean_data.csv")
asean = ['Philippines','Brunei','Cambodia','Indonesia','Malaysia','Myanmar','Singapore','Thailand','Vietnam']
aseancode = ['PHL','BRN','KHM','IDN','MYS','MMR','SGP','THA','VNM']
#print(df)
###GRAPHICS

rgdp_cri = df.loc[(df['country_x']=='Singapore') & (df['year_x']==2011)].rgdpo.values
df['gen_rgdpo'] = df['rgdpo']/ rgdp_cri * 100

#share of consumptiom gov and house
df['share_con'] = df['ccon']/ df['rgdpo']

#level of consumption
con_cri = df.loc[(df['country_x']=='Singapore') & (df['year_x']==2011)].rgdpo.values
df['gen_ccon'] = df['ccon']/ con_cri * 100


##GDP AND GDP per Capita
def gdp():
    fig1 = plt.figure()
    fig1.suptitle('GDP and GDP Per Capita(Singaport in 2011 = 100)', size=18)
    plt.tight_layout()
    for i in range(len(asean)):
        X = df.loc[df['countrycode_x']==aseancode[i]].year_x
        Y = df.loc[df['countrycode_x']==aseancode[i]].gen_rgdpo
        Z = df.loc[df['countrycode_x']==aseancode[i]].ave_income
        ax = fig1.add_subplot(3,3,i+1)
        ax.plot(X, Y, label = 'GDP', color ='grey')
        ax.plot(X, Z, label = 'GDP Per Capita')
        ax.set_title(asean[i])
        ax.legend()
    plt.show()

#gdp()


##################
##Real Consumption
#################
def con():
    fig1 = plt.figure()
    fig1.suptitle('Left: The Level of Real consumption(Singapor RGDP in 2011 = 100)\nRight: The Share of Real consumption(%RGDP)',
                  size=18)
    plt.tight_layout()
    for i in range(len(asean)):
        X = df.loc[df['countrycode_x']==aseancode[i]].year_x
        Y = df.loc[df['countrycode_x']==aseancode[i]].gen_rgdpo
        Z = df.loc[df['countrycode_x']==aseancode[i]].gen_ccon
        W = df.loc[df['countrycode_x']==aseancode[i]].share_con
        ax1 = fig1.add_subplot(3,3,i+1)
        ax2 = ax1.twinx()
        ax1.plot(X, Y, label = 'RGDP', color ='grey')
        ax1.plot(X, Z, label = 'Level of Consumption')
        ax2.plot(X, W, label = 'Share of consumption % RGDP', color='red')
        ax1.tick_params(axis='y', labelcolor='grey')
        ax2.tick_params(axis='y', labelcolor='red')
        ax2.set_ylim(0,1.3)
        ax1.legend()
        ax1.set_title(asean[i])
    plt.show()

#con()
#print(df.country_x.unique())
#plot('GDP Per Capita(Singaport in 2011 = 100)', 'ave_income')


def fdi():
    fig1 = plt.figure()
    fig1.suptitle('Share of Net FDI % RGDP', size=18)
    plt.tight_layout()
    for i in range(len(asean)):
        X = df.loc[df['countrycode_x']==aseancode[i]].year_x
        Y = df.loc[df['countrycode_x']==aseancode[i]].gen_rgdpo
        Z = df.loc[df['countrycode_x']==aseancode[i]].fdi
        ax1 = fig1.add_subplot(3,3,i+1)
        ax2 = ax1.twinx()
        ax1.plot(X, Y, label = 'RGDP', color ='grey')
        ax2.plot(X, Z, label = 'Share of Net FDI % RGDP')
        ax1.tick_params(axis='y', labelcolor='grey')
        ax2.tick_params(axis='y')
        ax2.legend()
        ax1.set_title(asean[i])
    plt.show()

#fdi()


def plot(title, series):
    fig = plt.figure()
    fig.suptitle(title,size=18)
    plt.tight_layout()
    for i in range(len(asean)):
        X = df.loc[df['countrycode_x']==aseancode[i]].year_x
        Y = df.loc[df['countrycode_x']==aseancode[i]][series]
        ax = fig.add_subplot(3,3,i+1)
        ax.plot(X, Y)
        ax.set_title(asean[i])
    plt.show()

plot("human capital","hc")
#print(df.country_x.unique())



#Z = df.loc[df['countrycode']==asean[i]].csh_i
#W = df.loc[df['countrycode']==asean[i]].fdi
