# QuizMaster
QuizWiz is an innovative GenAI-powered tool designed to generate quizzes from any educational document with ease.

## Table of Contents

* [Overview](#overview)
  * [Brief Description](#brief-description)
  * [Why?](#why)
  * [Technologies Used](#technologies-used)
  * [Target Audience](#target-audience)
  * [Technical Architecture](#technical-architecture)
  * [Project Status](#project-status)
  * [Future Plans](#future-plans)
* [Installation](#installation)
* [Usage](#usage)
* [Model and Data](#model-and-data)
* [How to authenticate GCP to access APIs?](#How-to-authenticate-GCP-to-access-APIs)
* [Contributing](#contributing)
* [Acknowledgments](#acknowledgments)
* [Contact](#contact)


## Overview
QuizWiz is an innovative GenAI-powered tool designed to generate quizzes from any educational document with ease.
### Brief Description
QuizMaster is an AI powered quiz generator that can generate and assess Quizzes from any educational document with ease. User can upload any number of pdfs and enter the topic to generate quizzes and give the assessment. 
Say goodbye to manual quiz creation and hello to automated, efficient learning.
![Watch the video](preview.gif)

### Why?
+ **Limitations of the Human Brain and the Abundance of Data:** Firstly, the human brain tends to forget ideas, the information it has consumed, and the understanding it has built on the assimilated infromation. Quizzes are a very effective way of both learning and retaining the information.
+ **The Abundance of Data:** Secondly, creating quizzes can itself be a very challenging task. Imagine you are student and you want to make a quiz out of the five research papers you read on text embeddings. Now, imagine that you a professor and you teach three courses, each course has minimum five topics, and for each topic there are atleast three documents on an average to refer. In the latter case you would definitely not say no to an automatic quiz generator like QuizMaster.
### Technologies used
+ Langchain, Chroma DB, GCP, VertexAI, Gemini 1.5, Streamlit, HuggingFace

### Target Audience
+ Students
+ Teaching Assitants
+ Professors
+ Educators
+ E-Learning Platforms

### Technical Architecture
![Technical Architecture](technical_architecture.jpg)
+ DocumentProcessor : Renders a streamlit UI, allows users to upload multiple PDFs and processes them into pages using Langchain's PyPDFLoader.
+ ChromaCollectionCreator : Further breaks down the pages from Document Processor into chunks using Langchain's RecursiveCharacterTextSplitter. Uses embeddings from either VertexAI or locally from HuggingFace depending on user's choice. Also has the option to persist the DB onto local machine for later use.
+ QuizGenerator : Implements RAG by extractings chunks relevant to the topic from user, formulates a prompt, passes it to LLM, generates quizzes, validates the structure, and renders the quizzes through streamlit.
+ QuizManager : Facilitates moving from one question to another.

### Project Status
+ Phase 1 : Currently the project only supports uploading PDFs.

### Future Scope
+ Extend the capabilities of the the application to allow for uploading Youtube Videos, Podcasts, Links to URLs, and PDFs at the same time.
+ Host the app on a server
+ Make the data-ingestion system more robust

## Installation
> ** Python 3.10**
1. Clone this repository to your local machine using:
    ```bash
    $ git clone https://github.com/Dephinate/QuizMaster.git
    $ cd your_project
    ```
2. Create a conda environment and install dependencies
    ```bash
    $ pip install -r requirements.txt
    ```

## Usage
1. Need to first perform google authentication to use Gemini pro from Vertex AI.
2. To run the app copy the following command in your terminal:
    ```bash
    $ streamlit run src/user_interface/streamlitui.py
    ```
3. Upload PDFs, write the topic and give the quiz.

## Model and Data
For embeddings used: all-mpnet-base-v2/Embeddings from Vertex AI. 
LLM uses: Gemini Pro from Vertex AI

## How to authenticate GCP to access APIs?
Watch the video : https://www.loom.com/share/fa6cd412c1274683a0ebab5a43b09597?sid=bff89143-0997-426d-81ee-c3f0feea549f
## Contributing
Coming soon..

## Acknowledgments
https://www.lettria.com/blogpost/retrieval-augmented-generation-5-uses-and-their-examples
https://colabdoge.medium.com/what-is-rag-retrieval-augmented-generation-b0afc5dd5e79
https://www.hopsworks.ai/dictionary/vector-database

## Contact
[LinkedIn] (https://www.linkedin.com/in/vks2102/)
