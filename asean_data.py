import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pwt90_w_country_names.csv")
#print(df.head())
df = df[['countrycode','country','year','rgdpo',
         'hc', 'emp', 'ccon', 'cwtfp', 'pop',
         'csh_c','csh_i', 'csh_g', 'csh_x', 'csh_m']]

#print(df.tail())

##asean 
asean = ['BRN','KHM','IDN','MYS','MMR','PHL','SGP','THA','VNM']
#+sort by country
df = df.loc[df['year']>=1970]
df = df.loc[df['countrycode'].isin(asean)].sort_values(['country', 'year'])
df['ave_income'] = df['rgdpo']/ df['pop']

##generalize
capital_cri = df.loc[(df['country']=='Singapore') & (df['year']==2011)].csh_i.values
income_cri = df.loc[(df['country']=='Singapore') & (df['year']==2011)].ave_income.values
df['ave_income'] = df['ave_income']/ income_cri *100
df['csh_i'] = df['csh_i']/ capital_cri *100

print(df.country.unique())
print(df.countrycode.unique())
#df.to_csv("asean_pwt.csv", index=False)
