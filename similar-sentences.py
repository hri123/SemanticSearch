from sentence_transformers import SentenceTransformer, util

# https://huggingface.co/sentence-transformers?sort_models=downloads#models

# multi-qa-MiniLM-L6-cos-v1, nq-distilbert-base-v1, paraphrase-MiniLM-L12-v2
# this model seems best among what I tried, followed by all-mpnet-base-v2
model = SentenceTransformer('paraphrase-mpnet-base-v2')

query = 'Obama speaks to the media in Illinois'
# query = 'The cat sat on the mat'
query = 'IBM has employed me since long time'
query = 'Modi is in Bangalore'

passage = ['The cat sat on the mat', 
            'Obama speaks to the media in Illinois', 
            'The President greets the press in Chicago', 
            'The dog sat on the mat', 
            'The cat in the hat sat on the mat', 
            'The cat sat on the rug',
            'The mat was where the cat sat',
            'I am working at International Business Machines since 20 years']

query_embedding = model.encode(query)
passage_embedding = model.encode(passage)
cos_sim = util.cos_sim(query_embedding, passage_embedding)

for idx, sentence in enumerate(passage):
    if cos_sim[0][idx] > -10.4:
        print("Similarity: ", cos_sim[0][idx], ' ', sentence)








