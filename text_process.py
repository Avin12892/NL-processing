import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

class TextProcess(object):

    def __init__(self, raw_text):
        self.raw_text = raw_text
    
    def tokenizer(self, token_type=word_tokenize):
        '''word_tokenize or sent_tokenize'''
        self.raw_text = token_type(self.raw_text)
        

    def normalize(self):
        '''Need to explain the purpose of this, Jesse?'''
        tokens = nltk.word_tokenize(self.raw_text)
        return [word.lower() for word in tokens]


    def add_to_text(self, raw_text):
        self.raw_text += raw_text
    
