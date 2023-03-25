import global_variables as g
g.init() 

from utils import getSpacySentsFromFile, getLinesFromFile

def main():
    filename = '/Users/hrishikesh/H/GoogleDrive/OPO/Obsidian/DayJob/Projects/Lakehouse/Lakehouse-Root.md'
    # sentences = getSpacySentsFromFile(filename)
    sentences = getLinesFromFile(filename)


    query = 'The President greets the press in Chicago'
    query = "clustr accss"

    from fuzzy_search import printFuzz
    from rapidfuzz import process, fuzz
    # printFuzz(fuzz, process, query, sentences)

    from regex_search import printRegexImplementation3, printRegexImplementation4
    # printRegexImplementation3(query, sentences)
    # printRegexImplementation4()

    from sentence_transformer import printTestResults
    query = 'IBM has employed me since long time'
    # printTestResults(query, g.fixed_sentences)

    from spacy_search import printSpacyResults
    query = "cluster access"
    # printSpacyResults(query, sentences)

    from tf_idf_vectorizer import printTfIDFTest, get_tf_idf_query_similarity
    # printTfIDFTest(g.fixed_sentences)
    # query = "cluster access"
    # get_tf_idf_query_similarity(sentences, query)



# TODO: https://docs.haystack.deepset.ai/docs/answer_generator#example-of-openaianswergenerator-in-a-pipeline


if __name__ == "__main__":
    main()