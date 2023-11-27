from sentence_transformers import SentenceTransformer, util

# https://huggingface.co/sentence-transformers?sort_models=downloads#models

# multi-qa-MiniLM-L6-cos-v1, nq-distilbert-base-v1, paraphrase-MiniLM-L12-v2
# this model seems best among what I tried, followed by all-mpnet-base-v2


def printTestResults(query, sentences):
    model = SentenceTransformer('paraphrase-mpnet-base-v2')

    query_embedding = model.encode(query)
    passage_embedding = model.encode(sentences)
    cos_sim = util.cos_sim(query_embedding, passage_embedding)

    for idx, sentence in enumerate(sentences):
        if cos_sim[0][idx] > -10.4:
            print("Similarity: ", cos_sim[0][idx], ' ', sentence)

