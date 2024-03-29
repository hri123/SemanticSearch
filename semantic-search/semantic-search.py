#!/usr/bin/env python

# TODO: https://www.linkedin.com/feed/update/urn:li:activity:7044207398038708224/

# https://www.deepset.ai/blog/how-to-build-a-semantic-search-engine-in-python -> https://haystack.deepset.ai/tutorials/01_basic_qa_pipeline -> https://github.com/deepset-ai/haystack-tutorials/blob/main/tutorials/01_Basic_QA_Pipeline.ipynb


import logging

logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("haystack").setLevel(logging.INFO)




def testPrediction(retriever):

    from haystack.nodes import FARMReader

    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)


    from haystack import Pipeline

    querying_pipeline = Pipeline()
    querying_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
    querying_pipeline.add_node(component=reader, name="Reader", inputs=["Retriever"])


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



def testGeneration(retriever):

    # from haystack.nodes import OpenAIAnswerGenerator

    # generator = OpenAIAnswerGenerator(api_key=MY_API_KEY)


    from haystack.nodes import Seq2SeqGenerator

    generator = Seq2SeqGenerator(model_name_or_path="vblagoje/bart_lfqa")


    from haystack.pipelines import GenerativeQAPipeline

    generative_QA_pipeline = GenerativeQAPipeline(generator=generator, retriever=retriever)


    while True:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        query = input('Type your query: ')
        print('The user input is: ', query)

        # as per my observation the generated answer is not printing "good" answers as per me, so commenting it out for now

        result = generative_QA_pipeline.run(query=query, params={"Retriever": {"top_k": 5}})
        for idx, answer in enumerate(result['answers']):
            print('############ generated-answer ', idx, ' #################')
            print('answer: ', answer.answer)


def testSummarization(retriever):

    from haystack.pipelines import SearchSummarizationPipeline
    from haystack.nodes import BM25Retriever, TransformersSummarizer

    summarizer = TransformersSummarizer(model_name_or_path="sshleifer/distilbart-xsum-12-6", use_gpu=False)
    summarization_pipeline = SearchSummarizationPipeline(retriever=retriever, summarizer=summarizer, return_in_answer_format=True)


    while True:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        query = input('Type your query: ')
        print('The user input is: ', query)

        # as per my observation the summarization mostly is the same as the prediction, so commenting it out for now

        print('############ SUMMARIZATION #################')
        output = summarization_pipeline.run(
            query=query,
            params={
                "Retriever": {"top_k": 2},
            }
        )
        answers = output["answers"]
        # pprint(answers)
        for idx, answer in enumerate(answers):
            print('############ summary ', idx, ' #################')
            print('answer: ', answer['answer'])
            print('context: ', answer['context'])


def fillDocumentStore(document_store, doc_dir, respect_sentence_boundary=False):

    # https://haystack.deepset.ai/tutorials/08_preprocessing
    # from haystack.utils import print_documents
    # from pprint import pprint
    
    # from haystack.utils import convert_files_to_docs
    # all_docs = convert_files_to_docs(dir_path=doc_dir)
    # docs = preprocessor.process(all_docs)
    # document_store.write_documents(docs)

    from haystack.nodes import PreProcessor

    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=False,
        split_by="word", # 'word' / 'sentence' / 'passage'
        split_length=100, # 1000 seems to give better score but slow, 500 seems to give better answers than 200
        split_overlap=20,
        split_respect_sentence_boundary=respect_sentence_boundary,
    )


    from haystack.nodes import TextConverter
    from pathlib import Path
    import os

    # MarkdownConverter converts only the displayed contents and removes the hidden contents - e.g. the link url is removed from [Link text Here](https://link-url-here.org), so using TextConverter
    converterT = TextConverter(
        remove_numeric_tables=True,
        valid_languages=["en"]
    )

    for subdir, dirs, files in os.walk(doc_dir):
        for file in files:
            if file.endswith((".md")):
                md_doc = converterT.convert(file_path=Path(os.path.join(subdir, file)), meta={'name': file})
                proccessed_md_doc = preprocessor.process(md_doc)
                document_store.write_documents(proccessed_md_doc)
            # TODO: add converters for PDF documents, Text documents, etc.



def main():


    from haystack.document_stores import InMemoryDocumentStore

    document_store = InMemoryDocumentStore(use_bm25=True)


    # doc_dir = "data/game-of-thrones"
    doc_dir = "/Users/hrishikesh/Downloads/cheatsheets"
    doc_dir = "/Users/hrishikesh/H/GoogleDrive/OPO/Obsidian/DayJob/Projects/NZ-SaaS"
    # doc_dir = "/Volumes/Kaizen/ng-rb/RB-files/attitude/rb-md"

    
    fillDocumentStore(document_store, doc_dir, respect_sentence_boundary=False)
    
    
    from haystack.nodes import BM25Retriever

    retriever = BM25Retriever(document_store=document_store)

    # TODO: Can use pipeline instead too
    # from haystack.pipelines import Pipeline
    # from haystack.nodes import PreProcessor, TextConverter, Retriever
    # from haystack.nodes import DeepsetCloudDocumentStore

    # pipeline = Pipeline()
    # pipeline.add_node(component=text_converter, name="TextConverter", inputs=["File"])
    # pipeline.add_node(component=preprocessor, name="PreProcessor", inputs=["TextConverter"])
    # pipeline.add_node(component=retriever, name="EmbeddingRetriever", inputs=["PreProcessor"])
    # pipeline.add_node(component=document_store, name="DeepsetCloudDocumentStore", inputs="EmbeddingRetriever")



    testPrediction(retriever)
    # testGeneration(retriever)
    # testSummarization(retriever)


if __name__ == "__main__":
    main()