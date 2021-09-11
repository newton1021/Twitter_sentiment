#!/usr/bin/env python

from tweet_db import Tweet_api 
from database import DataBase as DB
import my_Learning as myl

import pandas as pd
import numpy as np



if __name__ == "__main__":
	
	tw = Tweet_api()
	tw.connect_to_twitter()
	
	
	db = DB()
	
	# get tweets
	
	topics = ["ABBA", "texas", "puppy", "war"]
	
	for topic in topics:
		results = tw.getTweets(topic)
		
		db.saveDataset_postgres(results, topic)
	
	df = db.getCurrentData()
	
	df = myl.processData(df)
	
	df = myl.calcSentiment(df)
	
	myl.createModel(df)
	
	db.updateDatabase(df)
		