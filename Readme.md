# Restrict answers to the data in the folder

https://stackoverflow.com/a/76241713/512126

# TODO:

Three things that can be done by AI:
- query - ask a question and answer
- search - find text as is using semantic search
- summarize - summarize a section of the text
- generate / create - TODO


Read:
- https://platform.openai.com/docs/guides/prompt-engineering
- https://platform.openai.com/docs/guides/embeddings/use-cases - Text search using embeddings
    - see if you can use pandas to read plain text file into dataframe
    - https://stackoverflow.com/a/75192794/512126
    - https://github.com/samwit/langchain-tutorials/blob/main/RAG/YT_Chat_your_PDFs_Langchain_Template_for_creating.ipynb


- https://github.com/alejandro-ao/ask-multiple-pdfs
- https://github.com/alejandro-ao/langchain-ask-pdf



- [ ] Write code to split files into different granularity levels
  - [ ] sentences
  - [ ] paragraphs
  - [ ] sections (multiple paragraphs)
- [ ] Associate each of the split parts with
  - [ ] tags / indexes / keywords
- [ ] Now come up with the ability to search each split part that matches the search pattern with scores
  - [ ] regex matches
  - [ ] semantic matches




- check bookmarks
- spaCy
- NLP
- Sentence similarity
- cosine similarity
- etc



# API Usage limits

- https://platform.openai.com/usage


# Different ways to search for what you need from knowledge base

- fuzzy search
- semantic search (cosing similarity)
- query using openAI


# Using Tools and Editors

- using obsidian
	- find multiple words on a single line but in no particular order - `line:(universe go well examples)`
	- https://help.obsidian.md/Plugins/Search

- using fzf
	```
	brew install fzf
	brew install ripgrep
	
	rg --heading --line-number . /Volumes/Kaizen/ng-rb/RB-files/attitude/rb-md/  | fzf --layout=reverse
	```
	- https://github.com/rlivings39/vscode-fzf-quick-open
	- https://dev.to/iggredible/how-to-search-faster-in-vim-with-fzf-vim-36ko
	- `vim "$(fzf)"` - Open file after searching

- Silver Search
	- look ahead search / ag silver search : `^(?=.?wealth)(?=.?health).*$`
	- works in vscode