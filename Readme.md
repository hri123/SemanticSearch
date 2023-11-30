# Different ways to search for what you need from knowledge base

- fuzzy search
- semantic search without openAI APIs (NLP, spacy, cosine similarity)
- query / search with openAI APIs
    - query - ask a question and let it answer the question
    - search - find text as is using semantic search
    - summarize - summarize a section of text
    - generate / create - generate code, essay


## My understanding of the best way to search for what you need from knowledge base

- **quick search** - use fuzzy search using rg and fzf

- when you want to **query something** - go over this in detail - https://betterprogramming.pub/building-a-multi-document-reader-and-chatbot-with-langchain-and-chatgpt-d1864d47e339
    - using embeddings help send only the relevant chunks as tokens to the openAI API
        - https://stackoverflow.com/questions/74000154/how-do-i-make-sure-answers-are-from-a-customized-fine-tuning-dataset/75192794#75192794
        - https://www.youtube.com/watch?v=8kJStTRuMcs
        - https://community.openai.com/t/answering-lots-of-questions-from-one-large-chunk-of-text-without-paying-tokens-to-input-the-big-text-chunk-for-each-question/323843/8



# references

## openai API Usage limits

- https://platform.openai.com/usage


## Examples of using openai APIs for semantic search

- https://github.com/samwit/langchain-tutorials/blob/main/RAG/YT_Chat_your_PDFs_Langchain_Template_for_creating.ipynb
https://github.com/alejandro-ao/ask-multiple-pdfs - uses streamlit for GUI

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

# TODO:

## Read:

- https://platform.openai.com/docs/guides/prompt-engineering
- https://platform.openai.com/docs/guides/embeddings/use-cases - Text search using embeddings




