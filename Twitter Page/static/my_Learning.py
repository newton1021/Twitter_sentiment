#!/usr/bin/env python

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

import warnings
warnings.filterwarnings("ignore")

import nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import string
import pandas as pd
import numpy as np
import re
import enchant
d = enchant.Dict("en_US")


def preprocess_tweet_text(tweet):
	
	tweet = tweet.lower()
	
	tweet = re.sub(r"http\S+|www\S+|https\S+","",tweet, flags=re.MULTILINE)   
	
	tweet = tweet.translate(str.maketrans("","",string.punctuation))
	
	tweet = re.sub(r'\@\w+|\#\'',"",tweet)
	
	tweet_tokens = word_tokenize(tweet)
	filtered_words = []
	filtered_words = []
	for word in tweet_tokens:
		if (d.check(word)) & (word not in stop_words):
			filtered_words.append(word)
		else:
			continue
	
	
	
#     ps = PorterStemmer()
#     stemmed_words = [ps.stem(w) for w in filtered_words]
	
	lemmatizer = WordNetLemmatizer()
	lemma_words = [lemmatizer.lemmatize(w, pos='a') for w in filtered_words]
	
	return " ".join(lemma_words)

def processData(dataset):
	dataset.tweet_cleaned = dataset.tweet_text.apply(preprocess_tweet_text)
	return dataset

def get_feature_vector(train_fit):
	vector = TfidfVectorizer(sublinear_tf=True)
	vector.fit(train_fit)
	return vector


def int_to_string(sentiment):
	if sentiment < -0.1:
		return "Negative"
	elif sentiment < 0.1:
		return "Neutral"
	else:
		return "Positive"
	
	
	
def calcSentiment(dataset):
	sent = []
	for x in dataset['tweet_cleaned']:
		blob_object = TextBlob(x)
		
		analysis = blob_object.sentiment
		
		s = analysis.subjectivity
		p = analysis.polarity
		
		
		print(analysis)
		
		if p < -0.1:
			r = -1
		elif p > 0.1:
			r = 1
		else:
			r = 0
		sent.append(r) 
		
	#create the sentiment column
	dataset["est_positivity"] = sent
	return dataset
	
	
	
def createModel(dataset):
	
	dataset.tweet_cleaned = dataset.tweet_text.apply(preprocess_tweet_text)
	
	# setup transform for tweet
	tf_vector = TfidfVectorizer(ngram_range=(1,2), max_features=500000)
	
	
	#separate tweets that do not have a sentiment
	test = [pd.isna(x) for x in dataset['est_positivity']]
	dataset1 = dataset[test]
	tested = [not x for x in test]
	dataset2 = dataset[tested]
	
	
	
	#fit the vector with the tested tweets.
	tf_vector.fit(np.array(dataset2['tweet_cleaned']).ravel())
	
	#transform the datasets 
	X = tf_vector.transform(np.array(dataset2['tweet_cleaned']).ravel())
	if any(test):
		X_n = tf_vector.transform(np.array(dataset1['tweet_cleaned']).ravel())
	else:
		X_n = []
		
	y = np.array(dataset2['est_positivity']).ravel()
	# y = y.astype('float')
	
	#create training set and test set
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=30)
	
	
	# Training Logistics Regression model
	LR_model = LogisticRegression(solver='lbfgs')
	LR_model.fit(X_train, y_train)
	y_predict_lr = LR_model.predict(X_test)
	print(accuracy_score(y_test, y_predict_lr))
	
		
	if len(X_n) > 0:
		y_n = LR_model.predict(X_n)
		y_n = y_n.reshape(-1,1)
		dataset1['est_positivity'] = y_n
		return dataset1
	else:
		return X
	
	

	
	
	
	