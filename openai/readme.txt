# Init

virtualenv env
source /Users/hrishikesh/C/git/github.com/SemanticSearch/openai/env/bin/activate
pip install embedchain
pip install --upgrade "embedchain[dataloaders]"

# for gpt4all

pip install gpt4all


# troubleshooting

- chromadb.errors.InvalidDimensionException: Embedding dimension 1536 does not match collection dimensionality 384
    - rm /Users/hrishikesh/C/SandBoxes/Search/embedchain/db

- The model `gpt-35-turbo` does not exist
    - gpt-3.5-turbo

- Must provide one of the `base_url` or `azure_endpoint` arguments, or the `AZURE_OPENAI_ENDPOINT` environment variable (type=value_error)
    - deployment_name: ec_embeddings_ada_002 in openai.yaml to be commented

# API Usage limits

- https://platform.openai.com/usage

# How to runbook

export OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
python main.py

# docs

- https://platform.openai.com/docs/guides/text-generation
- https://docs.embedchain.ai/get-started/examples
- https://github.com/openai/openai-python - code generation