import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("final_fdi.csv")
df2 = pd.read_csv("final_data.csv")


df= pd.merge(df1, df2, on='key')

print(df.columns)

df = df.drop(['countrycode_y', 'country_y', 'year_y', 'key'], axis=1)

df.columns = ['countrycode', 'country', 'year', 'fdi', 'rgdpo', 'pop', 'csh_i', 'ave_income']


fdi_cri = df.loc[(df['countrycode']=='USA') & (df['year']==2011)].fdi.values
df['fdi'] = df['fdi']/ fdi_cri *100

print(df)

#df.to_csv("final_of_final.csv", index=False)
