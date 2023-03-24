# TODO: https://course.spacy.io/en/
# https://spacy.io/models
# pip install spacy
# python -m spacy download en_core_web_lg

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


# List of sentences to compare
# sentences = ['The cat sat on the mat', 
#              'Obama speaks to the media in Illinois', 
#              'The President greets the press in Chicago', 
#              'The dog sat on the mat', 
#              'The cat in the hat sat on the mat', 
#              'The cat sat on the rug',
#              'The mat was where the cat sat']

# query = 'The cat sat on the mat'
# query = 'Obama speaks to the media in Illinois'

query = "cluster access"
query_processed = nlp(query)

for i in range(len(sentences)):
    sentence_processed = nlp(sentences[i])
    print("Similarity: ", query_processed.similarity(sentence_processed), ' ', sentences[i])
    print('-' * 20)


# TODO: https://github.com/gandersen101/spaczz

import spacy
from spaczz.matcher import FuzzyMatcher

nlp = spacy.blank("en")
text = """Grint Anderson created spaczz in his home at 555 Fake St,
Apt 5 in Nashv1le, TN 55555-1234 in the US."""  # Spelling errors intentional.
doc = nlp(text)

matcher = FuzzyMatcher(nlp.vocab)
matcher.add("NAME", [nlp("Grant Andersen")])
matcher.add("GPE", [nlp("Nashville")])
matches = matcher(doc)

for match_id, start, end, ratio in matches:
    print(match_id, doc[start:end], ratio)

import spacy
from spacy.tokens import Span
from spaczz.matcher import FuzzyMatcher

nlp = spacy.blank("en")
text = """Grint Anderson created spaczz in his home at 555 Fake St,
Apt 5 in Nashv1le, TN 55555-1234 in the US."""  # Spelling errors intentional.
doc = nlp(text)


def add_name_ent(matcher, doc, i, matches):
    """Callback on match function. Adds "NAME" entities to doc."""
    # Get the current match and create tuple of entity label, start and end.
    # Append entity to the doc's entity. (Don't overwrite doc.ents!)
    _match_id, start, end, _ratio = matches[i]
    entity = Span(doc, start, end, label="NAME")
    doc.ents += (entity,)


matcher = FuzzyMatcher(nlp.vocab)
matcher.add("NAME", [nlp("Grant Andersen")], on_match=add_name_ent)
matches = matcher(doc)

for ent in doc.ents:
    print((ent.text, ent.start, ent.end, ent.label_))

import spacy
from spaczz.matcher import FuzzyMatcher

nlp = spacy.blank("en")
# Let's modify the order of the name in the text.
text = """Anderson, Grint created spaczz in his home at 555 Fake St,
Apt 5 in Nashv1le, TN 55555-1234 in the US."""  # Spelling errors intentional.
doc = nlp(text)

matcher = FuzzyMatcher(nlp.vocab)
matcher.add("NAME", [nlp("Grant Andersen")])
matches = matcher(doc)

# The default fuzzy matching settings will not find a match.
for match_id, start, end, ratio in matches:
    print(match_id, doc[start:end], ratio)

import spacy
from spaczz.matcher import FuzzyMatcher

nlp = spacy.blank("en")
# Let's modify the order of the name in the text.
text = """Anderson, Grint created spaczz in his home at 555 Fake St,
Apt 5 in Nashv1le, TN 55555-1234 in the US."""  # Spelling errors intentional.
doc = nlp(text)

matcher = FuzzyMatcher(nlp.vocab)
matcher.add("NAME", [nlp("Grant Andersen")], kwargs=[{"fuzzy_func": "token_sort"}])
matches = matcher(doc)

# The default fuzzy matching settings will not find a match.
for match_id, start, end, ratio in matches:
    print(match_id, doc[start:end], ratio)