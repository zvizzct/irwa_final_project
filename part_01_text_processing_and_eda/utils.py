import json
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from collections import defaultdict
from array import array
import numpy as np
import string


def convert_jsonlines_to_json(input_file, output_file):
    """
    Convert a .jsonl file to a .json file.

    Parameters:
    - input_file (str): Path to the input .jsonl file.
    - output_file (str): Path to the output .json file.
    """
    with open(input_file, 'r') as infile:
        data = [json.loads(line) for line in infile]

    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def build_terms(tweet):
    """
    Preprocess a tweet to extract terms.

    Parameters:
    - tweet (dict): A dictionary representing a tweet.

    Returns:
    - list: A list of preprocessed terms from the tweet.
    """
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words("english"))
    
    text = tweet['full_text'].lower()
    text = ''.join([char for char in text if char not in string.punctuation or char == '#'])
    text = text.split()
    text = [word for word in text if word not in stop_words]
    text = [stemmer.stem(word) for word in text]
    
    return text

def create_index(tweets):
    """
    Create an inverted index from a list of tweets.

    Parameters:
    - tweets (list): A list of dictionaries, each representing a tweet.

    Returns:
    - tuple: A tuple containing two dictionaries: the inverted index and the tweet index.
    """
    index = defaultdict(list)
    tweet_index = {}

    for tweet in tweets:
        tweet_id = tweet['id']
        terms = build_terms(tweet)
        tweet_text = tweet['full_text']
        tweet_index[tweet_id] = {
            'Tweet': tweet_text,
            'Date': tweet['created_at'],
            'Hashtags': [hashtag['text'] for hashtag in tweet['entities']['hashtags']],
            'Likes': tweet['favorite_count'],
            'Retweets': tweet['retweet_count'],
            'Url': f"https://twitter.com/i/web/status/{tweet_id}"
        }
        
        current_tweet_index = {}
        for position, term in enumerate(terms):
            try:
                current_tweet_index[term][1].append(position)
            except:
                current_tweet_index[term] = [tweet_id, array('I', [position])]

        for term_tweet, posting_tweet in current_tweet_index.items():
            index[term_tweet].append(posting_tweet)
    
    return index, tweet_index

def load_tweets(file_path):
    """
    Load tweets from a .json file.

    Parameters:
    - file_path (str): Path to the .json file containing tweets.

    Returns:
    - list: A list of dictionaries, each representing a tweet.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def search(query, index):
    """
    Search for a query in the inverted index.

    Parameters:
    - query (str): The search query.
    - index (dict): The inverted index.

    Returns:
    - list: A list of document IDs matching the query.
    """
    query = build_terms({"full_text": query})
    docs = set()
    for term in query:
        try:
            term_docs = [posting[0] for posting in index[term]]
            docs = docs.union(term_docs)
        except:
            pass
    docs = list(docs)
    return docs
