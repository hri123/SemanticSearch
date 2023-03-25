#!/usr/bin/env python

# TODO: https://www.linkedin.com/feed/update/urn:li:activity:7044207398038708224/

# https://www.deepset.ai/blog/how-to-build-a-semantic-search-engine-in-python -> https://haystack.deepset.ai/tutorials/01_basic_qa_pipeline -> https://github.com/deepset-ai/haystack-tutorials/blob/main/tutorials/01_Basic_QA_Pipeline.ipynb



# doc_dir = "data/game-of-thrones"
doc_dir = "/Users/hrishikesh/Downloads/cheatsheets"
doc_dir = "/Users/hrishikesh/H/GoogleDrive/OPO/Obsidian/DayJob/Projects/NZ-SaaS"
# doc_dir = "/Volumes/Kaizen/ng-rb/RB-files/attitude/rb-md"


import logging

logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("haystack").setLevel(logging.INFO)

from haystack.document_stores import InMemoryDocumentStore

document_store = InMemoryDocumentStore(use_bm25=True)


# https://haystack.deepset.ai/tutorials/08_preprocessing
from haystack.utils import convert_files_to_docs
from haystack.nodes import PreProcessor

all_docs = convert_files_to_docs(dir_path=doc_dir)

preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=False,
    split_length=500, # 1000 seems to give better score but slow, 500 seems to give better answers than 200
    split_overlap=20,
    split_respect_sentence_boundary=True,
)

docs = preprocessor.process(all_docs)
document_store.write_documents(docs)


from haystack.nodes import MarkdownConverter
from pathlib import Path
import os

converter = MarkdownConverter(
    remove_numeric_tables=True,
    valid_languages=["en"]
)

for subdir, dirs, files in os.walk(doc_dir):
    for file in files:
        if file.endswith((".md")):
            md_doc = converter.convert(file_path=Path(os.path.join(subdir, file)), meta={'name': file})
            proccessed_md_doc = preprocessor.process(md_doc)
            document_store.write_documents(proccessed_md_doc)

            





from haystack.nodes import BM25Retriever

retriever = BM25Retriever(document_store=document_store)


from haystack.nodes import FARMReader

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

from haystack import Pipeline

querying_pipeline = Pipeline()
querying_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
querying_pipeline.add_node(component=reader, name="Reader", inputs=["Retriever"])


# from haystack.nodes import OpenAIAnswerGenerator

# generator = OpenAIAnswerGenerator(api_key=MY_API_KEY)


from haystack.nodes import Seq2SeqGenerator

generator = Seq2SeqGenerator(model_name_or_path="vblagoje/bart_lfqa")

from haystack.pipelines import GenerativeQAPipeline

generative_QA_pipeline = GenerativeQAPipeline(generator=generator, retriever=retriever)


from pprint import pprint


from haystack.pipelines import SearchSummarizationPipeline
from haystack.nodes import BM25Retriever, TransformersSummarizer


summarizer = TransformersSummarizer(model_name_or_path="sshleifer/distilbart-xsum-12-6", use_gpu=False)
summarization_pipeline = SearchSummarizationPipeline(retriever=retriever, summarizer=summarizer, return_in_answer_format=True)


from haystack.utils import print_documents


while True:
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    query = input('Type your query: ')
    print('The user input is: ', query)

    prediction = querying_pipeline.run(
        query=query,
        params={
            "Retriever": {"top_k": 5},
            "Reader": {"top_k": 5}
        }
    )
    
    # pprint(prediction)

    print('############ PREDICTION #################')
    for idx, answer in enumerate(prediction['answers']):
        print('############ extracted-answer ', idx, ' #################')
        print('score: ', answer.score)
        print('answer: ', answer.answer)
        print('context: ', answer.context)
        print('meta: ', answer.meta)

    for idx, document in enumerate(prediction['documents']):
        print('############ document ', idx, ' #################')
        print('score: ', document.score)
        print('content: ', document.content)
        print('meta: ', document.meta)


    # as per my observation the generated answer is not printing "good" answers as per me, so commenting it out for now

    # result = generative_QA_pipeline.run(query=query, params={"Retriever": {"top_k": 5}})
    # for idx, answer in enumerate(result['answers']):
    #     print('############ generated-answer ', idx, ' #################')
    #     print('answer: ', answer.answer)

    # as per my observation the summarization mostly is the same as the prediction, so commenting it out for now

    # print('############ SUMMARIZATION #################')
    # output = summarization_pipeline.run(
    #     query=query,
    #     params={
    #         "Retriever": {"top_k": 2},
    #     }
    # )
    # answers = output["answers"]
    # # pprint(answers)
    # for idx, answer in enumerate(answers):
    #     print('############ summary ', idx, ' #################')
    #     print('answer: ', answer['answer'])
    #     print('context: ', answer['context'])
