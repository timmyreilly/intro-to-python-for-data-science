import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt

bdf = pd.read_csv("https://data.sfgov.org/api/views/5qua-egp2/rows.csv") # for bike lanes 
cdf = pd.read_csv("https://data.sfgov.org/api/views/q8d3-ck3z/rows.csv") # for street condition 


## Now let's build a basic view of our data 

c = cdf.loc[:,['Street_Name', 'PCI_Score']]
b = bdf.loc[:,['STREETNAME', 'FACILITY_T' ]]

b.columns = ['Street_Name', 'Lane_Type']

c['Street_Name'] = map(lambda x: x.upper(), c['Street_Name'])


d = pd.merge(b, c, on="Street_Name")

e = pd.merge(b, c, on="Street_Name", how="outer") 

dd = d.drop_duplicates() 
ee = e.drop_duplicates() 

# We don't really want to drop all of our dumplicates though... 
# we have 4802 rows 

f = d.loc[:,['Lane_Type', 'PCI_Score']]

# now we have bike paths, bike lanes, and bike routes + the score of the roads 

g = f.sort_values(by="Lane_Type")

h = g.loc[g['Lane_Type'] == 'BIKE ROUTE']
i = g.loc[g['Lane_Type'] == 'BIKE PATH']
j = g.loc[g['Lane_Type'] == 'BIKE LANE']

# Let's Check this out in a spreadsheet

g.to_csv('sample')

# Let's vizualize!

plt.boxplot(g) 

k = h.plot.box() 

plt.show() 
