"""
fuzzy_match.py

https://stackoverflow.com/questions/72017146/how-to-get-all-fuzzy-matching-substrings-between-two-strings-in-python

Dependent modules:
    pip install pandas
    pip install nltk
    pip install fuzzywuzzy
    pip install python-Levenshtein

"""


from nltk.util import ngrams
import pandas as pd
from thefuzz import fuzz


# Sample strings.
text1 = "Patient has checked in for abdominal pain which started 3 days ago. Patient was prescribed idx 20 mg every 4 hours."
text2 = "The time of discomfort was 3 days ago."
text3 = "John was given a prescription of idx, 20mg to be given every four hours"


def myprocess(st1: str, st2: str, threshold):
    """
    Generate sub-strings from st1 and compare with st2.
    The sub-strings, full string and fuzzy ratio will be saved in csv file.
    """
    data = []
    st1_length = len(st1.split())
    st2_length = len(st2.split())

    # Generate ngrams for string1
    m_start = 5
    for m in range(m_start, st1_length + 1):  # st1_length >= m_start

        # If m=3, fs1 = 'Patient has checked', 'has checked in', 'checked in for' ...
        # If m=5, fs1 = 'Patient has checked in for', 'has checked in for abdominal', ...
        for s1 in ngrams(st1.split(), m):
            fs1 = ' '.join(s1)
            
            # Generate ngrams for string2
            n_start = st2_length
            for n in range(n_start, st2_length + 1):
                for s2 in ngrams(st2.split(), n):
                    fs2 = ' '.join(s2)

                    fratio = fuzz.token_set_ratio(fs1, fs2)  # there are other ratios

                    # Save sub string if ratio is within threshold.
                    if fratio >= threshold:
                        data.append([fs1, fs2, fratio])

    return data


def get_match(sub, full, colname1, colname2, threshold=50):
    """
    sub: is a string where we extract the sub-string.
    full: is a string as the base/reference.
    threshold: is the minimum fuzzy ratio where we will save the sub string. Max fuzz ratio is 100.
    """   
    save = myprocess(sub, full, threshold)

    df = pd.DataFrame(save)
    if len(df):
        df.columns = [colname1, colname2, 'fuzzy_ratio']

        is_sort_by_fuzzy_ratio_first = True

        if is_sort_by_fuzzy_ratio_first:
            df = df.sort_values(by=['fuzzy_ratio', colname1], ascending=[False, False])
        else:
            df = df.sort_values(by=[colname1, 'fuzzy_ratio'], ascending=[False, False])

        df = df.reset_index(drop=True)

        df.to_csv(f'{colname1}_{colname2}.csv', index=False)

        # Print to console. Show only the sub-string and the fuzzy ratio. High ratio implies high similarity.
        df1 = df[[colname1, 'fuzzy_ratio']]
        print(df1.to_string())
        print()

        print(f'sub: {sub}')
        print(f'base: {full}')
        print()


def main():
    get_match(text2, text1, 'string2', 'string1', threshold=50)  # output string2_string1.csv
    get_match(text3, text1, 'string3', 'string1', threshold=50)

    get_match(text2, text3, 'string2', 'string3', threshold=10)

    # Other param combo.


if __name__ == '__main__':
    main()


import spacy
import pandas as pd


nlp = spacy.load("en_core_web_lg")

text1 = "Patient has checked in for abdominal pain which started 3 days ago. Patient was prescribed idx 20 mg every 4 hours."
text3 = "John was given a prescription of idx, 20mg to be given every four hours"

text3_sub = [
    'be given every four hours', 'idx, 20mg to be given every four hours',
    'was given a prescription of idx, 20mg to be given every four hours',
    'to be given every four hours',
    'John was given a prescription of idx, 20mg to be given every four hours',
    'of idx, 20mg to be given every four hours',
    'was given a prescription of idx, 20mg to be given every four',
    'prescription of idx, 20mg to be given every four hours',
    'given a prescription of idx, 20mg to be given every four hours',
    'a prescription of idx, 20mg to be given every four hours',
    'John was given a prescription of idx, 20mg to be given every four',
    'idx, 20mg to be given every',
    '20mg to be given every four hours'
]


data = []
for s in text3_sub:
    doc1 = nlp(s)
    doc2 = nlp(text1)
    sim = round(doc1.similarity(doc2), 3)
    data.append([s, text1, sim])

df = pd.DataFrame(data)
df.columns = ['from text3', 'text1', 'similarity']
df = df.sort_values(by=['similarity'], ascending=[False])
df = df.reset_index(drop=True)

df1 = df[['from text3', 'similarity']]
print(df1.to_string())

print()
print(f'text3: {text3}')
print(f'text1: {text1}')



from difflib import SequenceMatcher

text1 = "Patient has checked in for abdominal pain which started 3 days ago. Patient was prescribed idx 20 mg every 4 hours."
text2 = "The time of discomfort was 3 days ago."
text3 = "John was given a prescription of idx, 20mg to be given every four hours"


def fuzzy_match(t1: str, t2: str, min_len: int = 3, max_len: int = 10, ratio_to_get: int = 0.6):
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


if __name__ == '__main__':
    print(fuzzy_match(text1, text2))
    print(fuzzy_match(text2, text1))
    print(fuzzy_match(text1, text3))
    print(fuzzy_match(text3, text1))
    print(fuzzy_match(text2, text3))
    print(fuzzy_match(text3, text2))