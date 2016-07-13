#app.py 

import pandas as pd 
import numpy as np 
import matplotlib

bdf = pd.read_csv("https://data.sfgov.org/api/views/5qua-egp2/rows.csv") # for bike lanes 
cdf = pd.read_csv("https://data.sfgov.org/api/views/q8d3-ck3z/rows.csv") # for street condition 

print cdf.shape 
print cdf.columns 
print cdf.head(5)
print cdf.tail()

print bdf.shape
print bdf.columns
print bdf.head(5)


print cdf.dtypes # types 
print cdf.index 
print cdf.columns 
print cdf.values 

print cdf.describe() # Quick Statistical Summary 
print cdf.T # Transpose = rows become columns 

sorted_cdf = cdf.sort_values(by="Street_Name")

cdf_street_names = cdf['Street_Name']

cdf_street_names[2:15]


### Optimized Pandas Access Methods 
# Selecting by Label 
cdf.loc[:,['To_Street','From_Street','PCI_Score']] # Location Indexer 

#help(cdf.loc)

cdf.loc[175:200,['To_Street','From_Street','PCI_Score']]

### Selecting By Position 
# help(cdf.iloc)
cdf.iloc[3]

print cdf.iloc[3:5, 3:7]

cdf.iloc[[500, 1000, 10000], [2,3,4,1]] # using arrays for selection

print cdf.iloc[:,1:3]

### Boolean Indexing 

cdf[cdf['Street_Name'].isin(['Verna St'])] # Is this there? 

### Missing Data 

cdf2 = cdf.dropna(how='any') # Looking for any nan 

#### Operations!

### Stats 

cdf.mean() 

### Applying Functions 

cdf.loc[:,['PCI_Score']].apply(np.cumsum) 

### Join 

cdf2 = cdf.copy()
bdf2 = bdf.copy() 

df_joined = pd.merge(cdf2, bdf2) 

### Plotting
cdf_sort = cdf.sort_values(by="PCI_Score")

cdf_i = cdf_sort.loc[:,['To_Street', 'From_Street', 'PCI_Score']]


s = pd.Series(cdf_i.iloc[:, 2])


