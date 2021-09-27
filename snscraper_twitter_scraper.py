#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import snscrape.modules.twitter as sntwitter
import pandas as pd
from tqdm import tqdm
import datetime
import re

today = str(datetime.date.today())

# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list

keywords = ["#twitterspaces", "#spaces", "twitter spaces"] #set keywords for search, this searches all three twitter, spaces and twitter spaces
for key in tqdm(keywords):
    phrase = str(key) + ' since:2021-01-01 until:'+today #set search date range. Has to be in yyyy-mm-dd format
    #phrase = str(key) + ' since:2021-05-01 until:2021-05-10'
    print(phrase) #print date range for search
    
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(phrase).get_items()): #Use sntwitter to search for keywords in twitter
        #if i>500:
            #break
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.username])

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

#remove duplicate tweets
tweets_df = tweets_df.drop_duplicates('Tweet Id')

#save to csv file
directory = r"C:\Users\h00ns\Twitter Projects\Spaces\\"
file = str(directory)+str(keywords[0])+"_"+str(today)+"_Tweet_Data.csv"

tweets_df.to_csv(file, index= None)

print("Tweets saved as", file)


