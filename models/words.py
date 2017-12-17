import os
import nltk
import time
import main_script as ms


def get_common_words():
    file = 'docs' + os.sep + 'wiki-67k.txt'
    with open(file, 'r') as file:
        words = file.readlines()
    return {w.lower().strip(): True for w in words if not w.strip()[0] == '#'}


def get_pos(sentence):
    words_list = nltk.word_tokenize(sentence)
    new_list = []
    if len(words_list) == 0:
        return []
    for i in range(len(words_list)-1):
        if '\'' not in words_list[i] and 'n\'t' not in words_list[i+1]:
            new_list.append(words_list[i])
    if len(new_list) > 0 and '\'' not in words_list[-1]:
        new_list.append(words_list[-1])
    return nltk.pos_tag(new_list)


def filter_words(word_pos_list, common_words, my_words):
    # Returns list of words not in set w
    #print_my_words(my_words)
    toRet = []
    for w in word_pos_list:
        if (w[0] not in common_words):
            try:
                if (my_words[w[0]][2] < time.time() - ms.DEF_NOT_DISPLAYED_WITHIN_TIME
                    or my_words[w[0]][0] < ms.MAX_TIMES_WORD_DEF_DISPLAYED):
                    toRet.append(w)
            except KeyError:
                toRet.append(w)
    return toRet

def print_my_words(my_words):
    print('\nYour words:')
    pretty_print_defs(my_words)


def pretty_print_defs(my_words):
    for word in my_words.keys():
        s = my_words[word][1]
        s = s.replace("'", "")
        pos, part_of_speech, d = s[1:-1].split(':', 2)
        part_of_speech, junk = part_of_speech.split(",")
        part_of_speech = part_of_speech[1:]
        d = d[1:]
        print("%20s %-s " % ("Word: ", word))
        print("%20s %-s " % ("Part of Speech: ", part_of_speech))
        print("%20s %-s " % ("Times Defined: ", my_words[word][0]))
        print("%20s %-s " % ("Last Time Defined: ", time.ctime(my_words[word][2])))

        if(len(d) < 50):
            print("%20s %s" % ("Definition: ", d))
        else:
            print("%20s %s-" % ("Definition: ", d[:50]))
            d = d[50:]
            while(len(d) > 50):
                print("%20s %s-" % ("", d[:50]))
                d = d[50:]
            print("%20s %s" % ("", d))
        print("\n")

def pretty_print_words(lst):
    for l in lst:
        word, pos, d = l.split(":", 2)
        print("%20s %-s " % ("Word: ", word))
        print("%20s %-s " % ("Part of Speech: ", pos))
        if (len(d) < 50):
            print("%20s %s" % ("Definition: ", d))
        else:
            print("%20s %s-" % ("Definition: ", d[:50]))
            d = d[50:]
            while (len(d) > 50):
                print("%20s %s-" % ("", d[:50]))
                d = d[50:]
            print("%20s %s" % ("", d))
        print("\n")

