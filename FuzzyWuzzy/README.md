# search_in_files

## Semantic Search / Fuzzy Search - My Research

Fuzzy String Matching in Python:
https://github.com/seatgeek/fuzzywuzzy

How Fuzzy Wuzzy Works:
http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/
https://dirkmjk.nl/nl/node/397
https://marcobonzanini.com/2015/02/25/fuzzy-string-matching-in-python/

node library:
https://github.com/nol13/fuzzball.js
https://www.npmjs.com/package/fuzzball
https://github.com/NaturalNode/natural/tree/master/lib/natural/tokenizers

My Question in StackOverflow:
https://stackoverflow.com/questions/47605377/semantic-search-retrieve-sentences-from-a-bunch-of-text-files-that-closely-mat
He solved using LCS (Longest common subsequence) and autocorrect library, but I feel the fuzzywuzzy library is better to try

ElasticSearch:
https://www.youtube.com/watch?v=uK_dFzg63MU
https://www.youtube.com/watch?v=9UEymp254kA

What is semantic search:
https://www.r-bloggers.com/fuzzy-string-matching-a-survival-skill-to-tackle-unstructured-information/
http://docs.ipstreet.com/docs/concept-search

Similar Library:
FuzzySet: https://stackoverflow.com/questions/10383044/fuzzy-string-comparison/38316398#38316398

NLTK and Wordnet Usage in Python:
https://likegeeks.com/nlp-tutorial-using-python-nltk/

Linux Utility:
https://github.com/laurikari/tre/
https://stackoverflow.com/questions/9439121/fuzzy-file-search-in-linux-console/19805303#19805303

Search in stackoverflow:
- https://stackoverflow.com/search?q=search+that+can+match+verb+and+noun+form+of+the+word

Best answer:
- https://stackoverflow.com/questions/8716227/best-way-to-rank-sentences-based-on-similarity-from-a-set-of-documents/8716778#8716778

Lemmatization, Stemming:
- https://stackoverflow.com/questions/29277753/nlp-retrieve-vocabulary-from-text/29282868#29282868

URL fuzzy / semantic search:
- https://stackoverflow.com/questions/203278/are-clean-urls-a-backend-or-a-frontend-thing/206941#206941

Gensim (Generate Similar):
- https://radimrehurek.com/gensim/about.html

### Convert to a executable

http://www.mxm.dk/2008/02/python-eggs-simple-introduction.html

### Split into sentences yourself

https://stackoverflow.com/questions/4576077/python-split-text-on-sentences/31505798#31505798

## finds - line with moby and sauce and tartar in ANY ORDER

(lookahead search)

- ag with PCRE (Perl Compatible Regular Expression)
ag '(?=.*?m[^\s]+y)(?=.*?sauce)(?=.*?tartar)^.*$' /Users/hrishikesh/H/HP/Dropbox/Kaizen/ng-rb/RB-files/attitude/rb/
See https://regexr.com/3hnol for the explanation of each of the characters in the regular expression


NOTE: PCRE works in sublime text, did not work for me in visual studio code (https://stackoverflow.com/questions/42179046/what-flavor-of-regex-does-visual-studio-code-use/42184299#42184299)

- AWK
awk 'tolower($0) ~ /m[^\s]+y/ && tolower($0) ~ /sauce/ && tolower($0) ~ /tartar/' /Users/hrishikesh/H/HP/Dropbox/Kaizen/ng-rb/RB-files/attitude/rb/**/*.*

- grep

(use ag for now)

## Test your Regular Expressions

https://regexr.com

