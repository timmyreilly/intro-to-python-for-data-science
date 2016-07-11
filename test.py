import numpy as np 
import pandas as pd 
import datetime
import urllib

from bokeh.plotting import * 
from bokeh.models import HoverTool 
from collections import OrderedDict

import requests 

r = requests.get("https://data.sfgov.org/resource/q8d3-ck3z.json") # Street Conditions

b = requests.get("https://data.sfgov.org/resource/5qua-egp2.json") # Bike Lanes 

r = requests.get("https://data.sfgov.org/resource/q8d3-ck3z.json?$$app_token=FyHG9NaGt06NO7v2tYuYh1yKl")

condition = pd.read_json("https://data.sfgov.org/resource/q8d3-ck3z.json?$$app_token=FyHG9NaGt06NO7v2tYuYh1yKl")
lanes = pd.read_json("https://data.sfgov.org/resource/5qua-egp2.json")

l = requests.get("https://data.sfgov.org/api/views/5qua-egp2/rows.csv")
l = requests.get("https://data.sfgov.org/api/views/q8d3-ck3z/rows.csv")

l = requests.get("https://data.sfgov.org/api/views/q8d3-ck3z/rows.csv?$$app_token=FyHG9NaGt06NO7v2tYuYh1yKl")

import requests

headers = {'X-App-Token': TOKEN}

r = requests.get("https://data.sfgov.org/resource/q8d3-ck3z.json" , headers=headers)

condition_df = pd.read_csv("https://data.sfgov.org/api/views/5qua-egp2/rows.csv") # for street condition 
bike_df = pd.read_csv("https://data.sfgov.org/api/views/q8d3-ck3z/rows.csv") # for bike lanes

# We want to merge these files into a single csv with a 

