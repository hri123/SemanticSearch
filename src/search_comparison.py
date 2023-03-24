import global_variables as g
g.init() 

from utils import getSpacySentsFromFile

def main():
    filename = '/Users/hrishikesh/H/GoogleDrive/OPO/Obsidian/DayJob/Projects/Lakehouse/Lakehouse-Root.md'
    sentences = getSpacySentsFromFile(filename)


    query = 'The President greets the press in Chicago'
    query = "clustr accss"

    from fuzzy_search import printFuzz
    from rapidfuzz import process, fuzz
    # printFuzz(fuzz, process, query, sentences)

    from regex_search import printRegexImplementation3
    # printRegexImplementation3(query, sentences)


if __name__ == "__main__":
    main()