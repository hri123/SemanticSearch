# TODO: https://course.spacy.io/en/

# https://spacy.io/models
# pip install spacy
# python -m spacy download en_core_web_lg

import global_variables as g

def printSpacyResults(query, sentences):
    query_processed = g.nlp(query)

    for i in range(len(sentences)):
        sentence_processed = g.nlp(sentences[i])
        print("Similarity: ", query_processed.similarity(sentence_processed), ' ', sentences[i])
        print('-' * 20)


# TODO: https://github.com/gandersen101/spaczz
