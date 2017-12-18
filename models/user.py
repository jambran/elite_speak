class User(object):
    WORD_LIST = {}
    KNOWN_WORDS = {}

    def __init__(self, username, word_list, vocab_level):
        self.WORD_LIST = word_list
        self.KNOWN_WORDS = vocab_level
        self.username = username
        
    def get_known_words(self):
        return self.KNOWN_WORDS
        
    def add_to_known_words(self, word):
        self.KNOWN_WORDS.get(word,True)
        
    def get_username(self):
        return self.username
        
    def get_word_list(self):
        return self.WORD_LIST
        
    def append_to_word_list(self, word):
        self.WORD_LIST.get(word,True)