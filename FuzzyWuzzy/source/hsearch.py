# This file should only contain the logic, implementation details must be pushed into other files

# Move print help to a different file

# python3 hsearch.py "<search phrase>" "<files to include>"
# e.g.:
# python3 hsearch.py "hunt moby tartar" "/Users/H/HP/Dropbox/Kaizen/**/*.json"


import sys
import glob
from fuzzywuzzy import fuzz

search_phrase = sys.argv[1]
files_list = sys.argv[2]

# loop through each of the files

if __name__ == "__main__":
    for filename in glob.iglob(files_list, recursive=True):
        with open(filename, 'r') as myfile:

# split file into lines

            file_content = myfile.readlines()
            for line in file_content[0:]:
                ratio = fuzz.partial_ratio(search_phrase, line)
                if ratio > 60:
                    print(line)

            myfile.close()

# search phrase matches the lines ?

# print result

# TODO:

# simple search, regex search, fuzzy search, semantic search

# simple split at newline, split into english sentences

# print context - a few lines above and a few lines below

# search the search result, multiple piping

# indexing

