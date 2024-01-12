import os

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import pinecone

pinecone.init(api_key="4982f3b8-2cbb-453d-937a-7e4e6eb62bc0",environment="gcp-starter")

if __name__ == '__main__':
    print("Hello world")
    loader = TextLoader("./data/medium.txt")
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(len(texts))

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    docsearch = Pinecone.from_documents(texts,embeddings,index_name="gcp-medium-analyser")

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

    query="what is a vector DB? Give me a 15 word answer"
    result = qa({"query":query})
    print(result)
