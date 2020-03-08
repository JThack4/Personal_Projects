# -*- coding: utf-8 -*-
"""
Spyder Editor

I want to create a program to Automatically download fivethirty eights polling data and send me a table of all new general poll
results of the last week. This task is broken down into the folling steps:
    
    To have this run every week, use anacron
    
    1. Download data from website and load it into python
    2. Keep records with date of this week
    3. Create subtable with variables I want
    4. Send Email with table
    
"""
#importing necessary Packages
import requests
import os
from datetime import datetime
import glob
import pandas as pd



#Directory For Data
data_path = '/home/john/Documents/Programming/Data/fivethirtyeight_Polls2020Pres'

#defining Time. Want to name file based on the Monday its scheduled. 
today=datetime.today().strftime('%Y_%m_%d')

#Name of Datafile:
poll_file='president_polls_'+today+'.csv'


#Setting up download for downloading polling data
url = 'https://projects.fivethirtyeight.com/polls-page/president_polls.csv'
r = requests.get(url, allow_redirects=True)


#changing working directory to Data Directory
os.chdir(data_path)
print(os.curdir)
#get list of all files in directory

#get the latest file name prior to the new one being created.
list_of_files_old = glob.glob(data_path + '/*') # * means all if need specific format then *.csv
latest_file_old = max(list_of_files_old, key=os.path.getctime)



#writing file to directory
open(poll_file, 'wb').write(r.content)


#get the latest file name prior to the new one being created.
list_of_files_new = glob.glob(data_path + '/*') # * means all if need specific format then *.csv
latest_file_new = max(list_of_files_new, key=os.path.getctime)


#new file read ing
new_polls = pd.read_csv(latest_file_new) 
old_polls = pd.read_csv(latest_file_old)


new_polls1 = new_polls[['question_id','state','pollster','fte_grade','sample_size','population_full','methodology','start_date','end_date','created_at','stage','answer','pct']]
old_polls1  = old_polls[['question_id','state','pollster','fte_grade','sample_size','population_full','methodology','start_date','end_date','created_at','stage','answer','pct']]



new_polls1['time_create'] =  pd.to_datetime(new_polls1['created_at'])
old_polls1['time_create'] =  pd.to_datetime(old_polls1['created_at'])

#we know that the first row has most recent use this to 
oldmax=old_polls1[0,13]
print(old_polls1['time_create'].max())



type(new_polls1.at[0,'created_at'])
max_old=old_polls1['created_at'].max()
type(new_polls1['created_at'])