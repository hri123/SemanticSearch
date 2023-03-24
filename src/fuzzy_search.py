# https://github.com/seatgeek/thefuzz
# pip install thefuzz
# pip install python-Levenshtein

def printFuzzResultsTest(fuzz, process):
    print(fuzz.ratio("this is a test", "this is a test!"))
    print(fuzz.partial_ratio("this is a test", "this is a test!"))
    print(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))
    print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))
    print(fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
    print(fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
    print(fuzz.token_sort_ratio("fuzzy was a bear", "wuzzy fuzzy was a bear"))
    print(fuzz.partial_token_sort_ratio("fuzzy was a bear", "wuzzy fuzzy was a bear"))

    choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
    print(process.extract("new york jets", choices, limit=2))
    print(process.extractOne("cowboys", choices, scorer=fuzz.token_sort_ratio))

def testTheFuzzAndRapidFuzz():
    from thefuzz import fuzz
    from thefuzz import process

    printFuzzResultsTest(fuzz, process)

    from rapidfuzz import process, fuzz

    printFuzzResultsTest(fuzz, process)


def printFuzz(fuzz, process, query, sentences):
    print(process.extractOne(query, sentences))
    print(process.extractOne(query, sentences, scorer=fuzz.ratio))
    print(process.extractOne(query, sentences, scorer=fuzz.token_sort_ratio))
    print(process.extractOne(query, sentences, scorer=fuzz.token_set_ratio))
    print(process.extractOne(query, sentences, scorer=fuzz.partial_token_sort_ratio))
    print(process.extract(query, sentences, limit=4))

    print(process.extract(query, sentences, limit=4, scorer=fuzz.partial_ratio)) # best when fuzzy search multiple words in the same order, `clustr accss` and `cluster access`, but does not work if the query is `accss clustr`


