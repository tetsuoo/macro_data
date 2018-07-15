import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pwt90_w_country_names.csv")
#print(df.head())
data_set = df[['countrycode','country','year','rgdpo', 'pop','csh_i']]
#print(data_set.tail())

##eliminate aside from oecd
a = pd.read_csv("oecd_countries.csv")
oecd = a.countrycode
#test_countries = ["Australia","Japan","United Kingdom","United States"]
#oecd = test_countries
#+sort by country
data_set = data_set.loc[data_set['year']>=1970]
data_set = data_set.loc[data_set['countrycode'].isin(oecd)].sort_values(['country', 'year'])
data_set['ave_income'] = data_set['rgdpo']/ data_set['pop']

##generalize
capital_cri = data_set.loc[(data_set['countrycode']=='USA') & (data_set['year']==2011)].csh_i.values
income_cri = data_set.loc[(data_set['countrycode']=='USA') & (data_set['year']==2011)].ave_income.values
data_set['ave_income'] = data_set['ave_income']/ income_cri *100
data_set['csh_i'] = data_set['csh_i']/ capital_cri *100




#print(income_cri)
#print(data_set)


#print(data_set.year.head())
#print(str(data_set.year.head()))
##create merge key
print(data_set)

data_set.to_csv("edited_data.csv", index=False)
#
