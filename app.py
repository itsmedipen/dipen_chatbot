
import os# access my api key
import streamlit as st
from dotenv import load_dotenv #load api environment
from PyPDF2 import PdfReader# #get pdf text
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

#setting the api key environment and load the api key in environment
def main():
    load_dotenv()
    # print(os.getenv('GROQ_API_KEY'))#checking api key is loading or not
    groq_api_key = os.getenv('GROQ_API_KEY')
    
    #setting gpu
    st.set_page_config(page_title='Dipen AI chatbot 🧑')# title of the page
    
    st.header('Dipen AI Assistant 🧑')# header of the page
    questions =st.text_input('Ask any questions',placeholder='Ask anything')
    proces_click =st.button('Search',"Primary Button", type="primary")

    if questions and proces_click:
        with st.spinner('searching..'):#create spinner
                    # Embed documents
                embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                vectorstore = FAISS.from_texts(questions, embeddings)

                llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")
                st.session_state.qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
                response = st.session_state.qa_chain.run(questions)
                st.write("### 🧠🤖 Answer:")
                st.write(response)
        

if __name__ == '__main__':
    main()

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        left: 0;
        width: 100%;
        text-align: center;
        font-size: 0.9em;
        color: gray;
    }
    </style>
    <div class="footer">
        🧑Developed by <strong>Dipen Sherpa</strong>&nbsp;|&nbsp; © 2025
    </div>
    """,
    unsafe_allow_html=True
)








