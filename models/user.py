class User(object):
    WORD_LIST = {}
    VOCAB_LEVEL = 0

    def __init__(self, word_list, vocab_level):
        self.WORD_LIST = word_list
        self.VOCAB_LEVEL = vocab_level
        
    def get_word_list(self):
        return self.WORD_LIST
        
    def get_vocab_level(self):
        return self.VOCAB_LEVEL
        
    def set_vocab_level(self, level):
        vocab_level = level
        
    def append_to_word_list(self, word):
        word_list.append(word)