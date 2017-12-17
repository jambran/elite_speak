import os
import nltk
import time
import main_script as ms


def get_common_words():
    file = 'docs' + os.sep + 'new-wiki-100k.txt'
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
    return nltk.pos_tag(new_list)


def filter_words(word_pos_list, common_words, my_words):
    # Returns list of words not in set common_words
    toRet = []
    for w in word_pos_list:
        if(w[0] not in common_words):
            try:
                if(my_words[w[0]][2] < time.time() - ms.DEF_NOT_DISPLAYED_WITHIN_TIME
                   and my_words[w[0]][0] < ms.MAX_TIMES_WORD_DEF_DISPLAYED):
                    toRet.append(w)
            except KeyError:
                toRet.append(w)
    return toRet

