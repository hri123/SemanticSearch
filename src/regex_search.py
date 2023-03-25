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


# https://stackoverflow.com/a/72050412
def fuzzy_match_72050412(t1: str, t2: str, min_len: int = 3, max_len: int = 10, ratio_to_get: int = 0.6):
    from difflib import SequenceMatcher

    t1 = t1.replace(".", "").replace(",", "")
    t2 = t2.replace(".", "").replace(",", "")

    result = set()
    t2_splitted = t2.split(" ")
    t1_splitted = t1.split(" ")
    for count in range(min_len, max_len, 1):
        for pos_2 in range(len(t2_splitted) - count + 1):
            substr_2 = " ".join(t2_splitted[pos_2: pos_2 + count])
            for pos_1 in range(len(t1_splitted) - count + 1):
                substr_1 = " ".join(t1_splitted[pos_1: pos_1 + count])
                ratio = SequenceMatcher(None, substr_1, substr_2).ratio()
                if ratio >= ratio_to_get:
                    result.add(substr_1)

    return result


def printRegexImplementation4():
    text1 = "Patient has checked in for abdominal pain which started 3 days ago. Patient was prescribed idx 20 mg every 4 hours."
    text2 = "The time of discomfort was 3 days ago."
    text3 = "John was given a prescription of idx, 20mg to be given every four hours"


    print(fuzzy_match_72050412(text1, text2))
    print(fuzzy_match_72050412(text2, text1))
    print(fuzzy_match_72050412(text1, text3))
    print(fuzzy_match_72050412(text3, text1))
    print(fuzzy_match_72050412(text2, text3))
    print(fuzzy_match_72050412(text3, text2))