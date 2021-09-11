#!/Users/theDoctor/opt/anaconda3/envs/ PythonData




import pandas as pd	
import numpy as np  
import re 
import string

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


def load_dataset(filepath, cols):
	df = pd.read_csv(filepath, encoding='latin-1')
	df.columns = cols
	return df

def delete_redundant_cols(df, cols):
	for col in cols:
		del df[col]
		return df
	
def preprocess_tweet_text(tweet):
	
	tweet = tweet.lower()
	tweet = re.sub(r"http\S+|www\S+|https\S+","",tweet, flags=re.MULTILINE)   
	tweet = tweet.translate(str.maketrans("","",string.punctuation))
	tweet = re.sub(r'\@\w+|\#',"",tweet)
	
	tweet_tokens = word_tokenize(tweet)
	filtered_words = [word for word in tweet_tokens if word not in stop_words]
	
	ps = PorterStemmer()
	stemmed_words = [ps.stem(w) for w in filtered_words]
	
#	lemmatizer = WordNetLemmatizer()
#	lemma_words = [lemmatizer.lemmatize(w, pos='a') for w in stemmed_words]
	
	return " ".join(stemmed_words)




x = preprocess_tweet_text("Hi there, how are you preparing for your exams?")   

print(x)