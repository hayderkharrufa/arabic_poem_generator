# coding: utf-8
# author: Haydara  https://www.youtube.com/haydara

import pickle

with open('vocabs.pkl', 'rb') as pickle_load:
    voc_list = pickle.load(pickle_load)
    

allowed_chars = ['ذ', 'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'د',
                 'ش', 'س', 'ي', 'ب', 'ل', 'ا', 'أ', 'ت', 'ن', 'م', 'ك', 'ط', 'ئ', 'ء', 'ؤ', 'ر', 'ى', 
                 'ة', 'و', 'ز', 'ظ', 'ّ', ' ']

max_word_length = 9

def rhymes_with(word):
    if word not in ['الله', 'والله', 'بالله', 'لله', 'تالله']:
        word = word.replace('ّ', '')
    ending = word[-2:]
    rhymes = []
    for w in voc_list:
        if len(w) < max_word_length and w.endswith(ending):
            rhymes.append(w)
    return rhymes

def rhymes_with_last_n_chars(word, n):
    if word not in ['الله', 'والله', 'بالله', 'لله', 'تالله', 'فالله]:
        word = word.replace('ّ', '')
    ending = word[-n:]
    rhymes = []
    for w in voc_list:
        if len(w) < max_word_length and w.endswith(ending):
            rhymes.append(w)
    return rhymes
