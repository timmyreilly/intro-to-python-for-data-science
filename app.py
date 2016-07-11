#app.py 

import pandas as pd 

bdf = pd.read_csv("https://data.sfgov.org/api/views/5qua-egp2/rows.csv") # for bike lanes 
cdf = pd.read_csv("https://data.sfgov.org/api/views/q8d3-ck3z/rows.csv") # for street condition 

print cdf.shape 
print cdf.columns 
print cdf.head(5)

print bdf.shape
print bdf.columns
print bdf.head(5)


print cdf.dtypes 