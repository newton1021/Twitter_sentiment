#!/usr/bin/env python

import key_codes as keys
import webbrowser as web
import tweepy
from tweepy import OAuthHandler
import json
import re




class Tweet_api():
	
	def __init__ (self):
		api = []
		self.topic = "Monday"
	
	def connect_to_twitter(self):
	
		try:
			# create OAuthHandler object
			auth = OAuthHandler(keys.API_Key, keys.API_Secret)
			print("1...")
			# set access token and secret
			auth.set_access_token(keys.token, keys.secret)
			print("2...")
			# create tweepy API object to fetch tweets
			self.api = tweepy.API(auth)
			print("3...")
		except:
			print("Error: Authentication Failed")
			raise APIError("Failed to connect to twitter. Reautorize application")
		
		
	
	
	def authorize_twitter_app(self):
		redirect_url = auth.get_authorization_url()
		print("Go to website to authorize app")
		print(redirect_url)
		
		web.open(redirect_url)  # Go to example.com
		
		
		#get pin
		pin = input("Enter new PIN - ")
		
		try:
			auth.get_access_token(pin)
			print("token: " + auth.access_token )
			print("secret: " + auth.access_token_secret)
			self.api = tweepy.API(auth)
		except tweepy.TweepError:
			print('Error! Failed to get access token.')
			
			
	def getTweets(self,subject = ""):
		if subject == "":
			subject = self.topic
		else:
			self.topic = subject
			
			
		pattern = "RT @.*:"
		prog = re.compile(pattern)
				
		#results = api.search_30_day("BootCamp","mn state fair")
		
		jsonData = self.api.search(subject,count = 100,lang="en")
		dataset = []
		for r in jsonData:
			name  = r._json['user']['screen_name']
			createDate = r._json['created_at']
			retweet = r._json["retweeted"]
			if not retweet:
				try:
					tweet = r._json['extended_tweet']['full_text']
				except:
					tweet = r._json['text']
			if prog.search(tweet) is not None:
				continue
			else:
				print(tweet)
				data = f"{name}, {createDate}, {retweet}, {tweet}"
				dataset.append(data)
	#	filename = f"datasets/dataset {datetime.now().strftime('%Y%m%d%H_%M_%S')}.txt"
	#	textfile = open(filename, "w")
	#	for element in dataset:
	#		textfile.write(element + "\n")
	#	textfile.close()
		return dataset
	
