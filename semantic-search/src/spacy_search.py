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



def testSpacySimilarity():

    import pandas as pd
    
    text1 = "Patient has checked in for abdominal pain which started 3 days ago. Patient was prescribed idx 20 mg every 4 hours."
    text3 = "John was given a prescription of idx, 20mg to be given every four hours"

    text3_sub = [
        'be given every four hours', 'idx, 20mg to be given every four hours',
        'was given a prescription of idx, 20mg to be given every four hours',
        'to be given every four hours',
        'John was given a prescription of idx, 20mg to be given every four hours',
        'of idx, 20mg to be given every four hours',
        'was given a prescription of idx, 20mg to be given every four',
        'prescription of idx, 20mg to be given every four hours',
        'given a prescription of idx, 20mg to be given every four hours',
        'a prescription of idx, 20mg to be given every four hours',
        'John was given a prescription of idx, 20mg to be given every four',
        'idx, 20mg to be given every',
        '20mg to be given every four hours'
    ]


    data = []
    for s in text3_sub:
        doc1 = g.nlp(s)
        doc2 = g.nlp(text1)
        sim = round(doc1.similarity(doc2), 3)
        data.append([s, text1, sim])

    df = pd.DataFrame(data)
    df.columns = ['from text3', 'text1', 'similarity']
    df = df.sort_values(by=['similarity'], ascending=[False])
    df = df.reset_index(drop=True)

    df1 = df[['from text3', 'similarity']]
    print(df1.to_string())

    print()
    print(f'text3: {text3}')
    print(f'text1: {text1}')
