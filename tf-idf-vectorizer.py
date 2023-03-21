import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# The very first time of using stopwords from the NLTK package
# import nltk
# nltk.download('stopwords')

from nltk.corpus import stopwords
STOP_WORDS = list(stopwords.words('english'))

import nltk
STEMMER = nltk.stem.SnowballStemmer('english')
# STEMMER = nltk.stem.PorterStemmer()

# Preprocess function to tokenize, stem, and remove stop words from sentences
def preprocess(text):
    # Replace special characters and convert to lowercase
    text = text.lower().replace('\n', ' ').replace('\r', '')
    # Tokenize text and remove stop words
    tokens = [word for word in text.split() if word not in STOP_WORDS]
    # Stem words
    stemmed = [STEMMER.stem(token) for token in tokens]
    # Rejoin tokens into a single string
    text = ' '.join(stemmed)
    return text

# List of sentences to compare
sentences = ['The cat sat on the mat', 
             'Obama speaks to the media in Illinois', 
             'The President greets the press in Chicago', 
             'The dog sat on the mat', 
             'The cat in the hat sat on the mat', 
             'The cat sat on the rug',
             'The mat was where the cat sat']

# Preprocess sentences
processed_sentences = [preprocess(sentence) for sentence in sentences]

# Calculate TF-IDF vectors for the sentences
vectorizer = TfidfVectorizer()
tfidf_vectors = vectorizer.fit_transform(processed_sentences)

# Calculate cosine similarity matrix for the sentences
cosine_similarities = cosine_similarity(tfidf_vectors)

# Find duplicate sentences based on cosine similarity threshold
duplicate_threshold = 0.3
for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        if cosine_similarities[i][j] >= duplicate_threshold:
            print(f"Sentence {i+1} ({sentences[i]}) is a duplicate of sentence {j+1} ({sentences[j]}) with score {cosine_similarities[i][j]}")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_tf_idf_query_similarity(documents, query):
    docTFIDF = TfidfVectorizer(stop_words="english").fit_transform(documents)
    queryTFIDF = TfidfVectorizer(stop_words="english").fit(documents)
    queryTFIDF = queryTFIDF.transform([query])

    cosineSimilarities = cosine_similarity(queryTFIDF, docTFIDF)
    return cosineSimilarities

print(get_tf_idf_query_similarity(sentences, 'The cat sat on the mat'))

# TODO: https://course.spacy.io/en/
# https://spacy.io/models
# pip install spacy
# python -m spacy download en_core_web_lg

import spacy
nlp = spacy.load('en_core_web_lg')

query = 'The cat sat on the mat'
query = 'Obama speaks to the media in Illinois'

query_processed = nlp(query)

for i in range(len(sentences)):
    sentence_processed = nlp(sentences[i])
    print(query_processed.similarity(sentence_processed))