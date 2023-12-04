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

# returns average word length in a sentence
def average_length(text):
    words = text.split()
    total_letters = 0
    for word in words:
        total_letters += len(word)
    average_length = total_letters / len(words)
    return average_length

# returns a ratio of number of words starting w/ an upper case letter by total word count
def upper_count(text):
    words = text.split()
    upper_total = 0
    for word in words:
        if word.isupper():
            upper_total += 1
    upper_ratio = upper_total / len(words)
    return upper_ratio