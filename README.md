# Using Tools and Editors

- using obsidian
	- find multiple words on a single line but in no particular order - `line:(universe go well examples)`
	- https://help.obsidian.md/Plugins/Search

- using fzf
	```
	brew install fzf
	brew install ripgrep
	
	cd /Volumes/Kaizen/ng-rb/RB-files/attitude/rb-md
	
	rg --heading --line-number . | fzf --layout=reverse
	```
	- https://github.com/rlivings39/vscode-fzf-quick-open
	- https://dev.to/iggredible/how-to-search-faster-in-vim-with-fzf-vim-36ko
	- `vim "$(fzf)"` - Open file after searching

- Silver Search
	- look ahead search / ag silver search : `^(?=.?wealth)(?=.?health).*$`


# SemanticSearch

## Main Reference

- https://www.deepset.ai/blog/how-to-build-a-semantic-search-engine-in-python
- https://haystack.deepset.ai/tutorials/01_basic_qa_pipeline
- https://www.deepset.ai/blog/beyond-vanilla-question-answering-start-using-classification

## Other References:

- https://github.com/aws-samples/semantic-search-aws-docs
- https://opensemanticsearch.org/
- https://twitter.com/nucliaai
- https://datasciencedojo.com/blog/ai-powered-document-search/


## Setup


```
# install if not already installed
pip install virtualenv

# .../SemanticSearch
virtualenv env

source env/bin/activate

pip install --upgrade pip
pip install farm-haystack


# setup test data
mkdir -p data/game-of-thrones
cd data/game-of-thrones
wget https://s3.eu-central-1.amazonaws.com/deepset.ai-farm-qa/datasets/documents/wiki_gameofthrones_txt1.zip
unzip wiki_gameofthrones_txt1.zip
rm wiki_gameofthrones_txt1.zip


# for reading pdf files
pip install pdf2image
pip install pytesseract
brew install xpdf

# for reading markdown (md) files
pip install bs4
pip install python-frontmatter

# in case you want to use jupyter
pip install jupyter
jupyter notebook

```


# TODO

## Task

### Description

- [ ] Write code to split files into different granularity levels
  - [ ] sentences
  - [ ] paragraphs
  - [ ] sections (multiple paragraphs)
- [ ] Associate each of the split parts with
  - [ ] tags / indexes / keywords
- [ ] Now come up with the ability to search each split part that matches the search pattern with scores
  - [ ] regex matches
  - [ ] semantic matches

### Implementation

- check bookmarks
- spaCy
- NLP
- Sentence similarity
- cosine similarity
- etc
