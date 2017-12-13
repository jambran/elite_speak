import os
import nltk


def get_common_words():
    file = 'docs' + os.sep + 'wiki-100k.txt'
    with open(file, 'r') as file:
        words = file.readlines()
    return {w.lower().strip(): True for w in words if not w.strip()[0] == '#'}


def get_pos(sentence):
    words_list = nltk.word_tokenize(sentence)
    new_list = []
    for i in range(len(words_list)-1):
        if '\'' not in words_list[i] and 'n\'t' not in words_list[i+1]:
            new_list.append(words_list[i])
    if len(new_list) > 0 and '\'' not in words_list[-1]:
        new_list.append(words_list[-1])
    print(new_list)
    return nltk.pos_tag(new_list)


def filter_words(words, common_words):
    # Returns list of words not in set w
    return [w for w in words if w[0] not in common_words]