#!/usr/bin/env python


import pandas as pd
import numpy as np
import time

from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData, Integer
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session
Base = declarative_base()

class TweetData (Base):
	__tablename__ = "tweet_data"
	id = Column(Integer, primary_key = True)
	name = Column(String)
	date = Column(String)
	retweet_count = Column(Integer)
	tweet_text = Column(String)
	tweet_cleaned = Column(String)
	search_key = Column(String)
	est_positivity = Column(Integer)
	


class DataBase():
#	db_string = 'postgresql://postgres:drwho@localhost/twitter'
#	engine = create_engine(db_string)
#	Base.metadata.create_all(engine)
	
	def __init__(self):
		
		db_string = 'postgresql://postgres:drwho@localhost/twitter'
		self.db_string = db_string
		engine = create_engine(db_string)
		Base.metadata.create_all(engine)
		self.engine = engine
		

	def getCurrentData(self):
		dataset = pd.read_sql('tweet_data',con=self.engine) 
		return dataset
		
	def saveDataset_text(self, dataset):
		filename = f"../datasets/dataset {datetime.now().strftime('%Y%m%d%H_%M_%S')}.txt"
		textfile = open(filename, "w")
		for element in dataset:
			textfile.write(element + "\n")
		textfile.close()
		
		
	def saveDataset_postgres(self, results, search_key):
		#save results to db
		session = Session(bind=self.engine)
		for tweet in results:
			parts = tweet.split(',')
			if len(parts) > 2:
				newTweet = TweetData( name=parts[0], date = parts[1], retweet_count = 0, tweet_text = "".join(parts[3:]), search_key=search_key)
				session.add(newTweet)
		session.commit()
		session.close()
		
		
	
	def updateDatabase(self, dataset):
		session = Session(bind=self.engine)
		for index, row in dataset.iterrows():
			item = session.query(TweetData).filter(TweetData.id == row.id).first()
			item.tweet_cleaned = row.tweet_cleaned
			item.est_positivity = row.est_positivity
		session.commit()
		session.close()
			
			
	def getWordList(self):
		df = self.getCurrentData()
		pWords = []
		nWords = []
		pWords_set = set()
		nWords_set = set()
		dfp = df[df.est_positivity == 1]
		for ind, row in dfp.iterrows():
			wordlist = row.tweet_cleaned.split(" ")
			pWords += wordlist
			pWords_set.union(wordlist)
						
		dfn = df[df.est_positivity == -1]
		for ind, row in dfn.iterrows():
			wordlist = row.tweet_cleaned.split(" ")
			
			nWords += wordlist
			nWords_set.union(wordlist)
		
		return (pWords_set, pWords, nWords_set, nWords)
	
	def getPieData(self):
		df = self.getCurrentData()
		dfp = df[df.est_positivity == 1]
		dfn = df[df.est_positivity == -1]
		presults = dfp.groupby("search_key").count()
		p = presults[presults["search_key", "tweet_text"]]
		
		nresults = dfn.groupby("search_key").count()
		n = nresults[nresults["search_key", "tweet_text"]]
		return (p,n)
		
if __name__ == "__main__":
	db = DataBase()
	df = db.getCurrentData()
	df.head()