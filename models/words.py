import os
import nltk
import time
import main_script as ms
import random


def get_common_words(level):
    """
    Determines how many words the user knows based on their input. 
    Currently extremely rough estimates. Needs a lot of refining
    """
    fname = ""
    if level == '1':
        fname = "wiki-1500.txt"
    elif level == '2':
        fname = "wiki-20k.txt"
    elif level == '3':
        fname = "wiki-67k.txt"
    elif level == '4':
        return {w.lower().strip(): True for w in vocab_quiz() if not w.strip()[0] == '#'}
    else:
        print("Something went wrong with vocab list!")
        fname = "wiki-67k.txt"
    file = 'docs' + os.sep + fname
    with open(file, 'r') as file:
        words = file.readlines()
    return {w.lower().strip(): True for w in words if not w.strip()[0] == '#'}


def vocab_quiz():
    """
    Short quiz that randomly picks increasingly uncommon words. 
    When the user indicates they don't recognize a word, returns previous
    word as their vocabulary.
    """
    fname = "wiki-67k.txt"
    file = 'docs' + os.sep + fname
    with open(file, 'r') as file:
        words = file.readlines()
    
    i = 0
    while i < len(words):
        i = i + random.randrange(100,1000)
        rec = input("Do you know this word? (y/n): " + words[i])
        if rec.lower() == 'n':
            i = i - 1
            print("Vocabulary level set")
            break
        elif rec.lower() == 'y':
            continue
        else:
            while rec.lower() != 'y' and rec.lower() != 'n':
                rec = input("Unrecognized input. Please enter 'y' or 'n':")
    return words[:i]


def get_pos(sentence):
    """
    Uses nltk to determine the parts of speech for words in passed sentence
    """
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
    """
    Gets rid of words that shouldn't get definitions.
    """
    # Returns list of words not in set w
    # print_my_words(my_words)
    toRet = []
    for w in word_pos_list:
        # First gets rid of words in user's vocab
        if (w[0] not in common_words):
            try:
                # Also gets rid of words that have been recently defined or determined to 
                # have been learned.
                if (my_words[w[0]][2] < time.time() - ms.DEF_NOT_DISPLAYED_WITHIN_TIME
                    or my_words[w[0]][0] < ms.MAX_TIMES_WORD_DEF_DISPLAYED):
                    toRet.append(w)
            except KeyError:
                toRet.append(w)
    return toRet
  
    
def lemmatize(word, lemmatizer):
    """
    Lemmatizes a single word
    """
    return lemmatizer.lemmatize(word)


def lemmatize_words(words, lemmatizer):
    """
    Lemmatizes all words in a list
    """
    return [lemmatizer.lemmatize(word) for word in words]


def print_my_words(my_words):
    """
    Print all entries in my_words
    """
    print('\nYour words:')
    pretty_print_defs(my_words)
    return


def pretty_print_defs(my_words):
    """
    Prints all entries in my_words with pretty formatting
    """
    for word in my_words.keys():
        print("%20s %-s " % ("Word: ", word))
        print("%20s %-s " % ("Part of Speech: ", my_words[word][3]))
        print("%20s %-s " % ("Times Defined: ", my_words[word][0]))
        print("%20s %-s " % ("Last Time Defined: ", time.ctime(my_words[word][2])))
        d = my_words[word][1]
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
    return
        
def pretty_print_word(word, my_words):
    """
    Prints a single word with pretty formatting
    """
    print("%20s %-s " % ("Word: ", word))
    print("%20s %-s " % ("Part of Speech: ", my_words[word][3]))
    d = my_words[word][1]
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
    return
