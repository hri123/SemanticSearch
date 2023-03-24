# https://stackoverflow.com/q/17740833
import regex

def testRegex():
    input = "Monalisa was painted by Leonrdo da Vinchi"
    print(regex.search(r'\b(leonardo){e<3}\s+(da)\s+(vinci){e<2}\b', input, flags=regex.IGNORECASE))


def printRegexImplementation1(sentences):
    for i in range(len(sentences)):
        print('-' * 20)
        # print(sentences[i])
        print(regex.search(r'(cluster){e<3}(access){e<2}', sentences[i], flags=regex.IGNORECASE))
        print(regex.search(r'\b(clustr){e<3}\s+(accs){e<3}\b', sentences[i], flags=regex.IGNORECASE))
        print(regex.search(r"(?=.*hypershift)(?=.*access)", sentences[i], flags=regex.IGNORECASE)) # ignore order ?



def fuzzy_substring_search(major: str, minor: str, errs: int = 4):
    """Find the closest matching fuzzy substring.

    Args:
        major: the string to search in
        minor: the string to search with
        errs: the total number of errors

    Returns:
        Optional[regex.Match] object
    """
    errs_ = 0
    s = regex.search(f"({minor}){{e<={errs_}}}", major)
    while s is None and errs_ <= errs:
        errs_ += 1
        s = regex.search(f"({minor}){{e<={errs_}}}", major)
    return s

def printRegexImplementation2(query, sentences):
    for i in range(len(sentences)):
        print('-' * 20)
        print(fuzzy_substring_search(sentences[i], query))


def printRegexImplementation3(query, sentences):
    from difflib import SequenceMatcher as SM
    from nltk.util import ngrams
    import codecs

    for i in range(len(sentences)):
        print('-' * 20)
        needle = query
        hay    = sentences[i]

        needle_length  = len(needle.split())
        max_sim_val    = 0
        max_sim_string = u""

        for ngram in ngrams(hay.split(), needle_length + int(.2*needle_length)):
            hay_ngram = u" ".join(ngram)
            similarity = SM(None, hay_ngram, needle).ratio() 
            if similarity > max_sim_val:
                max_sim_val = similarity
                max_sim_string = hay_ngram
        print(max_sim_val, max_sim_string)
