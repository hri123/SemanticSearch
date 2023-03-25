import global_variables as g

def getFileAsText(filename):
    text_file = open(filename, "r")
    text = text_file.read() # read whole file to a string
    text_file.close()
    return text

def getSpacySents(text):
    emma = g.nlp(text).sents
    sentences = ["".join(str(list_of_words)) for list_of_words in emma]
    return sentences

def getSpacySentsFromFile(filename):
    text = getFileAsText(filename)
    sentences = getSpacySents(text)
    return sentences

def getLinesFromFile(filename):
    sentences = []
    with open(filename, 'r', encoding='UTF-8') as file:
        while (line := file.readline()):
            sentences.append(line.rstrip())
    return sentences