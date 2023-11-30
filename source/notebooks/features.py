from preprocess import preprocess

# count number of words in text
def count_words(text):
    return len(text.split())

# return ratio of unique to total words
def unique_ratio(text):
    words = text.split()
    unique_words = len(set(words)) / len(words)
    return unique_words

# list of common words in tabloids + top 20 total base words from buzzfeed, entertainment-weekly
sensational_words = ['Shocking','Exclusive','Scandal','Secrets','Revealed','Explosive',
'Bizarre','Sensational','Outrageous','Forbidden','Terrifying','Stunning','Jaw-Dropping',
'Unbelievable','Extraordinary','Suddenly','Shockingly','Secretly','Allegedly',
'Dramatically','Mysteriously','Surprisingly','Eerily','Incredibly','Unexpectedly']

sensational_words = ' '.join(sensational_words)
sensational_words = preprocess(sensational_words)
sensational_words = sensational_words + 'product gift thing make thatll season new realli home day start want youll peopl say movie one get'
sensational_words = sensational_words.split()