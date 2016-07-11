import pandas as pd 

import numpy as np 

import matplotlib

bdf = pd.read_csv("https://data.sfgov.org/api/views/5qua-egp2/rows.csv") # for bike lanes 
cdf = pd.read_csv("https://data.sfgov.org/api/views/q8d3-ck3z/rows.csv") # for street condition 


## Now let's build a basic view of our data 

c = cdf.loc[:,['Street_Name', 'PCI_Score']]
b = bdf.loc[:,['STREETNAME', 'FACILITY_T' ]]

b.columns = ['Street_Name', 'Lane_Type']

c['Street_Name'] = map(lambda x: x.upper(), c['Street_Name'])
# b['Street_Name'] = map(lambda x: x.upper(), b['Street_Name'])


d = pd.merge(b, c, on="Street_Name")

e = pd.merge(b, c, on="Street_Name", how="outer") 

dd = d.drop_duplicates() 
ee = e.drop_duplicates() 