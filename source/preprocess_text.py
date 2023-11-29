import pandas as pd
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# creating feature for number of words in each headline
def count_words(text):
    return len(text.split())

# creating feature for a ratio of unique words to total words in a headline
def unique_ratio(text):
    words = text.split()
    unique_words = len(set(words)) / len(words)
    return unique_words

def preprocess(text):
    # converts to lowercase
    text = text.lower()
    
    # removes puncutation
    text = text.translate(str.maketrans('','',string.punctuation))
    text = ''.join(char for char in text if char.isalpha() or char.isspace()) 
  
    # tokenizes words
    tokens = word_tokenize(text)
    
    # removes stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # lemmatizes, stems words into base forms
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    tokens = [stemmer.stem(token) for token in tokens]
    
    # combines tokens into a sentence again
    processed_text = ' '.join(tokens)
    
    return processed_text

# commonly found words in tabloids joined w/ top 20 base words from buzzfeed, ew
sensational_words = ['Shocking','Exclusive','Scandal','Secrets','Revealed','Explosive',
'Bizarre','Sensational','Outrageous','Forbidden','Terrifying','Stunning','Jaw-Dropping',
'Unbelievable','Extraordinary','Suddenly','Shockingly','Secretly','Allegedly',
'Dramatically','Mysteriously','Surprisingly','Eerily','Incredibly','Unexpectedly']

sensational_words = ' '.join(sensational_words)
sensational_words = preprocess(sensational_words)
sensational_words = sensational_words + 'product gift thing make thatll season new home day realli youll want say star peopl get one first'
sensational_words = list(sensational_words.split(' '))
sensational_words