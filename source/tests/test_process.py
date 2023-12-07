from features import average_length, count_words, sensational_words, unique_ratio, upper_count

def test_average_length():
    sentence = 'who liz might be seeing today'
    assert average_length(sentence) == 4.0

def test_unique_ratio1():
    sentence ='can i tell you a little secret'
    assert unique_ratio(sentence) == 1.0

def test_unique_ratio2():
    sentence ='super sally sells some seashells by the super sea shore'
    assert unique_ratio(sentence) == 0.9

def test_count_words():
    sentence = 'Israeli airstrikes on Gaza resume after weeklong truce with Hamas ends'
    assert count_words(sentence) == 11

def test_upper_words():
    sentence = 'Israeli airstrikes on Gaza resume after weeklong truce with Hamas ends'
    assert upper_count(sentence) == 3/11