import nltk
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize, word_tokenize
from text_process import TextProcess

class NLData(object):

    def __init__(self, raw_text):
        self.raw_text = raw_text
    
    

    def word_frequency(self):
        pass
    
        
    def chunck_passage(self, regex):
        for i in self.raw_text:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
            chunkParser = nltk.RegexpParser(regex)
            chunked = chunkParser.parse(tagged)
            chunked.draw()  

if __name__ == '__main__':

    #~ file = open("text.txt")
    #~ text_process = TextProcess(file.read())
    
    
    sample_text = state_union.raw("2006-GWBush.txt")
    text_process = TextProcess(sample_text)
    text_process.add_to_text( ' Testing this function!')
    text_process.tokenizer(sent_tokenize)
    result = text_process.raw_text

    
    trial = NLData(result)
    trial.chunck_passage(r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}""")
