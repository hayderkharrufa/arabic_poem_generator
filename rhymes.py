# coding: utf-8
# author: Haydara  https://www.youtube.com/haydara

import pickle

with open('vocabs.pkl', 'rb') as f:
    voc_list = pickle.load(f)

max_word_length = 9


def rhymes_with_last_n_chars(word, n):
    ending = word.replace('ّ', '')[-n:]
    return [w for w in voc_list if len(w) < max_word_length and w.endswith(ending)]


def rhymes_with(word):
    return rhymes_with_last_n_chars(word, 2)
