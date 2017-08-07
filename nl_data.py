import nltk

class NLData(object):

    def __init__(self, raw_text):
        self.raw_text = raw_text


    def word_frequency(self):
        pass


if __name__ == '__main__':

    file = open("/Users/Jesse/Code/Python workspace/Text Analysis/text.txt")

    textAnalysis = TextAnalysis(raw_text = file.read())
    print(textAnalysis.words)
