from os import environ
from dotenv import load_dotenv
from llama_index.core import (
        SimpleDirectoryReader,
        VectorStoreIndex,
        StorageContext,
        load_index_from_storage,
    )
from llama_index.llms.openai import OpenAI

from query import query

def main():
    load_dotenv()
    OPENAI_API_KEY = environ["OPENAI_API_KEY"]

    
    llm = OpenAI(model="gpt-4")

    custom_rules_docs = SimpleDirectoryReader(
        input_files=["./constant/custom_rules_1.0.md"]
    ).load_data()
    scanning_result_docs = SimpleDirectoryReader(
        input_files=["./constant/qualys_sample_report.json"]
    ).load_data()

    custom_index = VectorStoreIndex.from_documents(custom_rules_docs, show_progress=True)
    scan_index = VectorStoreIndex.from_documents(scanning_result_docs, swow_progress=True)

    print(custom_rules_docs)
    custom_index.storage_context.persist(persist_dir="./constant/custom_rules")
    scan_index.storage_context.persist(persist_dir="./constant/scan_results")
    
    query(custom_index, scan_index, llm)
    

if __name__ == "__main__":
    main()
    
