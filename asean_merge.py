import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("asean_fdi.csv")
df2 = pd.read_csv("asean_pwt.csv")

df= pd.merge(df1, df2, on='key')

print(df.columns)

df = df.drop(['countrycode_y', 'country_y', 'year_y', 'key'], axis=1)

print(df)

#df.to_csv("asean_data.csv", index=False)
