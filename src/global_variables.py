import spacy

def init():
    global nlp
    nlp = spacy.load('en_core_web_lg')
