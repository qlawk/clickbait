import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# preprocesses text for natural language processing
def preprocess(text):
    # converts to lowercase
    text = text.lower()
    
    # removes puncutation, non-alphabetical words
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