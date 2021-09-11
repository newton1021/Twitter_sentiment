#!/usr/bin/env python3

import tweepy
import json
from datetime import datetime

from keyCode import API_Key, API_Secret

auth = tweepy.OAuthHandler(API_Key, API_Secret)


def authorizeTweepy():
	
	try:
		redirect_url = auth.get_authorization_url()
	except tweepy.TweepError:
		print('Error! Failed to get request token.')
	print(redirect_url)
	
	session.set('request_token', auth.request_token['oauth_token'])
	
	verifier = request.GET.get('oauth_verifier')
	
	
	pin = "9735818"
	
	try:
		auth.get_access_token(pin)
	except tweepy.TweepError:
		print('Error! Failed to get access token.')
		
	return tweepy.API(auth)



def getTweets(subject, api):
	#results = api.search_30_day("BootCamp","mn state fair")
	
	global jsonData 
	jsonData = api.search(subject,count = 100,lang="en")
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
				
				
			data = f"{name}, {createDate}, {retweet}, {tweet}"
			dataset.append(data)
	return dataset



def saveDataset_text(dataset):
	filename = f"../datasets/dataset {datetime.now().strftime('%Y%m%d%H_%M_%S')}.txt"
	textfile = open(filename, "w")
	for element in dataset:
		textfile.write(element + "\n")
	textfile.close()


def saveDataset_postgres(dataset):
	filename = f"../datasets/dataset {datetime.now().strftime('%Y%m%d%H_%M_%S')}.txt"
	textfile = open(filename, "w")
	for element in dataset:
		textfile.write(element + "\n")
	textfile.close()
	
	
	
	
