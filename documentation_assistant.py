import os
from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



def ingest_docs()->None:
    loader = ReadTheDocsLoader(path="data/langchain_documentation/python.langchain.com/docs")
    raw_documents = loader.load()
    print("number of documents loaded = ",  len(raw_documents))
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50, separators=["\n\n", "\n", " ", ""])
    documents = text_splitter.split_documents(documents=raw_documents)
    print("splitter into = ", len(documents))


if __name__ == '__main__':
    ingest_docs()
