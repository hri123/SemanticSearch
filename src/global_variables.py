import spacy

def init():
    global nlp
    nlp = spacy.load('en_core_web_lg')

    global fixed_sentences
    fixed_sentences = ['The cat sat on the mat', 
             'Obama speaks to the media in Illinois', 
             'The President greets the press in Chicago', 
             'The dog sat on the mat', 
             'The cat in the hat sat on the mat', 
             'The cat sat on the rug',
             'The mat was where the cat sat']
