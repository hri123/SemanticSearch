# https://github.com/seatgeek/thefuzz
# pip install thefuzz
# pip install python-Levenshtein

from thefuzz import fuzz
from thefuzz import process

# from rapidfuzz import process, fuzz


"""
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
"""

sentences = ['The cat sat on the mat', 
             'Obama speaks to the media in Illinois', 
             'The President greets the press in Chicago', 
             'The dog sat on the mat', 
             'The cat in the hat sat on the mat', 
             'The cat sat on the rug',
             'The mat was where the cat sat']

query = 'The President greets the press in Chicago'



import spacy
nlp = spacy.load('en_core_web_lg')


file = '/Users/hrishikesh/H/GoogleDrive/OPO/Obsidian/DayJob/Projects/Lakehouse/Lakehouse-Root.md'
#open text file in read mode
text_file = open(file, "r")
#read whole file to a string
text = text_file.read()
#close file
text_file.close()


emma = nlp(text).sents
sentences = ["".join(str(list_of_words)) for list_of_words in emma]

query = "clustr accss"

print(process.extractOne(query, sentences))
print(process.extractOne(query, sentences, scorer=fuzz.ratio))
print(process.extractOne(query, sentences, scorer=fuzz.token_sort_ratio))
print(process.extractOne(query, sentences, scorer=fuzz.token_set_ratio))
print(process.extractOne(query, sentences, scorer=fuzz.partial_token_sort_ratio))
print(process.extract(query, sentences, limit=4))

print(process.extract(query, sentences, limit=4, scorer=fuzz.partial_ratio)) # best when fuzzy search multiple words in the same order, `clustr accss` and `cluster access`, but does not work if the query is `accss clustr`


# https://stackoverflow.com/q/17740833
import regex

# input = "Monalisa was painted by Leonrdo da Vinchi"
# print(regex.search(r'\b(leonardo){e<3}\s+(da)\s+(vinci){e<2}\b',input,flags=regex.IGNORECASE))


# for i in range(len(sentences)):
#     print('-' * 20)
#     # print(sentences[i])
#     print(regex.search(r'(cluster){e<3}(access){e<2}', sentences[i], flags=regex.IGNORECASE))
#     print(regex.search(r'\b(clustr){e<3}\s+(accs){e<3}\b', sentences[i], flags=regex.IGNORECASE))
#     print(regex.search(r"(?=.*hypershift)(?=.*access)", sentences[i], flags=regex.IGNORECASE)) # ignore order ?



# def fuzzy_substring_search(major: str, minor: str, errs: int = 4):
#     """Find the closest matching fuzzy substring.

#     Args:
#         major: the string to search in
#         minor: the string to search with
#         errs: the total number of errors

#     Returns:
#         Optional[regex.Match] object
#     """
#     errs_ = 0
#     s = regex.search(f"({minor}){{e<={errs_}}}", major)
#     while s is None and errs_ <= errs:
#         errs_ += 1
#         s = regex.search(f"({minor}){{e<={errs_}}}", major)
#     return s

# query = "clustr accs"

# for i in range(len(sentences)):
#     print('-' * 20)
#     print(fuzzy_substring_search(sentences[i], query))



# from difflib import SequenceMatcher as SM
# from nltk.util import ngrams
# import codecs

# query = "accss clustr"

# for i in range(len(sentences)):
#     print('-' * 20)
#     needle = query
#     hay    = sentences[i]

#     needle_length  = len(needle.split())
#     max_sim_val    = 0
#     max_sim_string = u""

#     for ngram in ngrams(hay.split(), needle_length + int(.2*needle_length)):
#         hay_ngram = u" ".join(ngram)
#         similarity = SM(None, hay_ngram, needle).ratio() 
#         if similarity > max_sim_val:
#             max_sim_val = similarity
#             max_sim_string = hay_ngram
#     print(max_sim_val, max_sim_string)




