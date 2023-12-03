# python3 fuzzySearch.py "compete with only yourself" "/Users/hrishikesh/H/HP/Dropbox/Kaizen/ng-rb/RB-files/attitude/rb/**/*.json" 80 5| more
# python3 fuzzySearch.py "tmux new window" "/Users/hrishikesh/C/GitHub/MyRepo/Projects/**/*.md" 70 5 | more

from fuzzywuzzy import process
from fuzzywuzzy import utils
from fuzzywuzzy import fuzz

import sys
import glob
import sys
import json
# -*- coding: utf-8 -*-
import re

from nltk.tokenize import sent_tokenize
import nltk

#do the following once

#nltk.download('punkt')
#sudo pip3 install -U nltk
#pip3 install -U python-Levenshtein
#pip3 install --upgrade pip
#pip3 install -U fuzzywuzzy

caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub("w.r.t.","",text)
    text = re.sub("e.g.","",text)
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

file_as_string=""
def walk(node):
    global file_as_string
    for key, item in node.items():
        if isinstance(item, dict):
            walk(item)
        elif key == "main":
            file_as_string += ".".join(item)
        elif isinstance(item, list):
            for x in item:
                walk(x)
        else:
            file_as_string += item

#mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

# search term: bahv
#mylist=["baloon", "Bhavs grape juice 8000087", "broom stick", "black swan", "The quick brown fox jumped over the lazy dog"]

#search_phrase="anyby jealouse ghost"
#search_phrase="GHOST OF JEALOUSY"

search_phrase=sys.argv[1]
files_list=sys.argv[2]
min_score=int(sys.argv[3])
limit_val=int(sys.argv[4])

for filename in glob.iglob(files_list, recursive=True):
    with open(filename, 'r') as myfile:
# Logic 1
#        mytext=myfile.read().replace('\n', '').replace('"', '').replace(',', '.').replace("{", '').replace("}", '').replace("[", '').replace("]", '')

# Logic 2: Very slow when there are too many files
        json1_as_dict = json.load(myfile)
        file_as_string=""
        walk(json1_as_dict)
        mytext=file_as_string

        myfile.close()
  
# Logic 1
#    mylist=sent_tokenize(mytext)

# Logic 2
    mylist1=split_into_sentences(mytext)
    # https://regexr.com/3hfo2
    regex = re.compile('^(\w)(?![ ]+\.)[\w\s]+\.$')

#    partial_token_sort_ratio - seems to be the best scorer based on my various tests
#    scorers=[fuzz.ratio, fuzz.partial_ratio, fuzz.token_sort_ratio, fuzz.partial_token_sort_ratio, fuzz.token_set_ratio, fuzz.partial_token_set_ratio, fuzz.QRatio, fuzz.UQRatio, fuzz.WRatio, fuzz.UWRatio]
    scorers=[fuzz.partial_token_sort_ratio]

    for i,ratio_type in enumerate(scorers):
#        print(ratio_type.__name__)
        mylist = filter(regex.search, mylist1)
        extracted=process.extractBests(search_phrase, mylist, processor=utils.full_process, scorer=ratio_type, score_cutoff=min_score, limit=limit_val)
#        extracted=process.extract(search_phrase, mylist, processor=utils.full_process, scorer=ratio_type, limit=5)
#        extracted=process.extractWithoutOrder(search_phrase, mylist, processor=utils.full_process, scorer=ratio_type, score_cutoff=20)
#        extracted=process.extractOne(search_phrase, mylist, processor=utils.full_process, scorer=ratio_type, score_cutoff=20)
        if len(extracted) > 0:
            print("*********************filename: ", filename)
        for result in extracted:
            print(result)
#        print("*****")
