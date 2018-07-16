import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fdi = pd.read_csv("fdi_flow.csv")
fdi.columns = ['country','countrycode','fdi','1970','1971','1972',
 '1973','1974','1975','1976','1977','1978','1979','1980','1981','1982',
 '1983','1984','1985','1986','1987','1988','1989','1990','1991','1992',
 '1993','1994','1995','1996','1997','1998','1999','2000','2001','2002',
 '2003','2004','2005','2006','2007','2008','2009','2010','2011','2012',
 '2013','2014','2015','2016','2017']

asean = ['BRN','KHM','IDN','MYS','MMR','PHL','SGP','THA','VNM']

fdi = fdi.loc[fdi['countrycode'].isin(asean)]

#print(fdi.columns)
#print('countrycode:',fdi.countrycode.values[0])
#print('\ncountry:', fdi.country.values[0])
#print('\nyear:', fdi.columns[3:])
#print('\nfdi flow:', fdi.ix[0,3:])

new_fdi = pd.DataFrame({'countrycode':np.repeat(fdi.countrycode.values[0],len(fdi.columns[3:])),
                        'country':np.repeat(fdi.country.values[0],len(fdi.columns[3:])),
                        'year':fdi.columns[3:],
                        'fdi':fdi.iloc[0,3:]})

#'fdi flow': fdi.ix[0,3:]
#print(fdi[0,:])


for i in range(len(fdi)):
    if(i>=1):
        df = pd.DataFrame({'countrycode':np.repeat(fdi.countrycode.values[i],len(fdi.columns[3:])),
                                    'country':np.repeat(fdi.country.values[i],len(fdi.columns[3:])),
                                    'year':fdi.columns[3:],
                                    'fdi':fdi.iloc[i,3:]})
        new_fdi = new_fdi.append(df)


new_fdi['key'] = new_fdi.countrycode.str.cat(new_fdi.year, sep='-')
print(type(new_fdi.countrycode))
print(type(new_fdi.countrycode.str))
print(type(new_fdi.year))
#print(new_fdi)

#new_fdi.to_csv("asean_fdi.csv", index=False)
#print(new_fdi.country.unique())
#print(new_fdi.countrycode.unique())
