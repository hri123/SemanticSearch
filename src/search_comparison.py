import global_variables as g
g.init() 

from utils import getSpacySentsFromFile

def main():
    filename = '/Users/hrishikesh/H/GoogleDrive/OPO/Obsidian/DayJob/Projects/Lakehouse/Lakehouse-Root.md'
    sentences = getSpacySentsFromFile(filename)


    print(sentences)

if __name__ == "__main__":
    main()