# TODO: https://course.spacy.io/en/
# https://spacy.io/models
# pip install spacy
# python -m spacy download en_core_web_lg

import spacy
nlp = spacy.load('en_core_web_lg')


file = '/Users/hrishikesh/H/GoogleDrive/OPO/Obsidian/DayJob/Projects/Lakehouse/Lakehouse-Root.md'
#open text file in read mode
text_file = open(file, "r")
#read whole file to a string
text = text_file.read()
#close file
text_file.close()


emma = nlp(text).sents
sentences = ["".join(str(list_of_words)) for list_of_words in emma]


# List of sentences to compare
# sentences = ['The cat sat on the mat', 
#              'Obama speaks to the media in Illinois', 
#              'The President greets the press in Chicago', 
#              'The dog sat on the mat', 
#              'The cat in the hat sat on the mat', 
#              'The cat sat on the rug',
#              'The mat was where the cat sat']

# query = 'The cat sat on the mat'
# query = 'Obama speaks to the media in Illinois'

query = "cluster access"
query_processed = nlp(query)

for i in range(len(sentences)):
    sentence_processed = nlp(sentences[i])
    print("Similarity: ", query_processed.similarity(sentence_processed), ' ', sentences[i])
    print('-' * 20)

