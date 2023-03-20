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
duplicate_threshold = 0.5
for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        # if cosine_similarities[i][j] >= duplicate_threshold:
            print(f"Sentence {i+1} ({sentences[i]}) is a duplicate of sentence {j+1} ({sentences[j]}) with score {cosine_similarities[i][j]}")