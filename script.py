import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import statsmodels.tsa.stattools as ts

df = pd.read_csv("final_of_final.csv")

a = pd.read_csv("oecd_countries.csv")
oecd = a.countrycode

df = df.sort_values(by=['countrycode','year'])
df['growth_rate'] = df.groupby('countrycode')['ave_income'].apply(lambda x: x.pct_change())
df = df.dropna()

def ols_reg(X,Y,country):
    #print('\nc ',country)
    result = sm.OLS(Y, sm.add_constant(X)).fit()
    print(country,result.params[1],result.pvalues[1])

def fire_growth_rate():
    for i in range(len(oecd)) :
        ols_reg(df.loc[df['countrycode']==oecd[i]].year, df.loc[df['countrycode']==oecd[i]].growth_rate,oecd[i])

def fire_csh_i():
    for i in range(len(oecd)) :
        ols_reg(df.loc[df['countrycode']==oecd[i]].year, df.loc[df['countrycode']==oecd[i]].csh_i,oecd[i])


def fire_fdi():
    for i in range(len(oecd)) :
        ols_reg(df.loc[df['countrycode']==oecd[i]].year, df.loc[df['countrycode']==oecd[i]].fdi,oecd[i])


#fire_fdi()

growth_rate_dummy =[0,0	,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
fdi_dummy = [1,1,0,1,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1]
csh_dummy = [1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1]

#print(len(growth_rate_dummy), len(fdi_dummy), len(csh_dummy))


def adf_result(timeseries, country, dummy):
    if dummy==1:
        result = ts.adfuller(timeseries.dropna(),regression='c')
    else:
        result = ts.adfuller(timeseries.dropna(),regression='ct')
    print(country, result,"\n")

def fire_adf_growth_rate():
    for i in range(len(oecd)) :
        adf_result(df.loc[df['countrycode']==oecd[i]].growth_rate,oecd[i],growth_rate_dummy[i])

#fire_adf_growth_rate()


def fire_adf_csh_i():
    for i in range(len(oecd)) :
        adf_result(df.loc[df['countrycode']==oecd[i]].csh_i,oecd[i],csh_dummy[i])

#fire_adf_csh_i()


def fire_adf_growth_rate():
    for i in range(len(oecd)) :
        adf_result(df.loc[df['countrycode']==oecd[i]].fdi,oecd[i],fdi_dummy[i])

#fire_adf_growth_rate()



adf_result(df.loc[df['countrycode']=='CZE'].fdi,'CZE',1)
aaaa = df.loc[df['countrycode']=='CZE']
