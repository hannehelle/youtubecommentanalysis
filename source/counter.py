import re
import collections


def words_counter(text):
    words = ''.join(text)
    
    word_list = re.findall(r"[А-я]+|[\w']", words.lower())

    words_counter = collections.Counter(word_list)
    comments_words_counter = dict(words_counter)
    
    return words_counter