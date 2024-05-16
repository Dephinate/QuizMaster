# embedding_client.py
import streamlit as st
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings


class EmbeddingClient:
    """
    Initialize the EmbeddingClient class to connect to Google Cloud's VertexAI for text embeddings with specific configurations
    for model name, project, and location. 

    Parameters:
    - model_name: A string representing the name of the model to use for embeddings.
    - project: The Google Cloud project ID where the embedding model is hosted.
    - location: The location of the Google Cloud project, such as 'us-central1'.
    """
    
    def __init__(self, model_name, project, location):
        # Initialize the VertexAIEmbeddings client with the given parameters
        # Read about the VertexAIEmbeddings wrapper from Langchain here
        # https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai
        self.client = VertexAIEmbeddings(
            #### YOUR CODE HERE ####
            location = location,
            model_name = model_name,
            project = project
        )
        
    def embed_query(self, query):
        """
        Uses the embedding client to retrieve embeddings for the given query.

        :param query: The text query to embed.
        :return: The embeddings for the query or None if the operation fails.
        """
        vectors = self.client.embed_query(query)
        return vectors
    
    def embed_documents(self, documents):
        """
        Retrieve embeddings for multiple documents.

        :param documents: A list of text documents to embed.
        :return: A list of embeddings for the given documents.
        """
        try:
            return self.client.embed_documents(documents)
        except AttributeError:
            print("Method embed_documents not defined for the client.")
            return None

class EmbeddingsHuggingFace:
    def __init__(self,model_name) :
        """
        Args:
            :param model_name: 
                relative path of the folder containing the config.json file. 
                Or
                name of the model on HuggingFace
        """
        self.model_name = model_name
        self.emembeddings = HuggingFaceEmbeddings(model_name=model_name)

    def download_embeddings_from_huggingface(self,model_name:str = None):
        """
        Retrive embeddings from HuggingFace or local
        Args:
            :param model_name: 
                relative path of the folder containing the config.json file. 
                Or
                name of the model on HuggingFace
        Example:  
            embeddings = HuggingFaceEmbeddings(model_name="./artifacts/embeddings/models--sentence-transformers--all-mpnet-base-v2/snapshots/84f2bcc00d77236f9e89c8a360a00fb1139bf47d")
        """
        model_name = model_name or self.model_name
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        return embeddings


if __name__ == "__main__":
    model_name = "textembedding-gecko@003"
    project = "rich-agency-421922"
    location = "us-central1"

    embedding_client = EmbeddingClient(model_name, project, location)
    vectors = embedding_client.embed_query("Hello World!")
    if vectors:
        st.header('Test Embeddings API')
        print(vectors)
        st.subheader('Hello World Embedding')
        st.write(vectors)
        print("Successfully used the embedding client!")
