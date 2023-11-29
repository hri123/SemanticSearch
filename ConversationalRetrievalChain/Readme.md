# Note:

- using langchain, a lower level library than embedchain to do the search


# Init

virtualenv env
source env/bin/activate
pip install langchain openai chromadb tiktoken unstructured
pip install "unstructured[pdf]"
pip install "unstructured[md]"

# How to run

export OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
python main.py

# references

https://github.com/techleadhd/chatgpt-retrieval/blob/main/README.md
https://python.langchain.com/docs/modules/data_connection/document_loaders/file_directory

