import streamlit as st
from streamlit_chat import message
from streamlit_pdf_viewer import pdf_viewer
import os
from rag import run  
from pdf_reader_fun import pdf_reader

# Set the page configuration
st.set_page_config(page_title="Text RAG Application", layout="wide")

# Title of the application
st.title("Text RAG Application")

# Sidebar for chat history
st.sidebar.title("Chat History")

# Initialize session state variables
if 'pdf_refs' not in st.session_state:
    st.session_state.pdf_refs = []
if 'vectordb' not in st.session_state:
    st.session_state.vectordb = None
if 'pdf_view' not in st.session_state:
    st.session_state.pdf_view = None
if "user_query_history" not in st.session_state:
    st.session_state["user_query_history"] = []
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

# Display chat history in the sidebar
with st.sidebar:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_query_history"],
    ):
        st.write(f"**User:** {user_query}")
        st.write(f"**Response:** {generated_response}")
        st.write("---")

# Upload PDF section
st.header("Upload & View PDFs")
uploaded_pdfs = st.file_uploader("Upload PDF files", type='pdf', accept_multiple_files=True, key='pdfs')

if uploaded_pdfs:
    st.session_state.pdf_refs = uploaded_pdfs

for pdf_ref in st.session_state.pdf_refs:
    if st.button(f"View {pdf_ref.name}"):
        st.session_state.pdf_view = pdf_ref

    if st.session_state.pdf_view == pdf_ref:
        binary_data = pdf_ref.getvalue()
        pdf_viewer(input=binary_data, width=700, height=600)

# Query input section
st.header("Query")
query = st.text_input("Enter your query here...", key='query', placeholder="Enter your query here...")

# Function to process PDFs and store them in the vector database
def process_pdfs_to_vectordb(pdf_refs):
    with st.spinner("Processing PDFs..."):
        pdf_directory = "pdfs"
        os.makedirs(pdf_directory, exist_ok=True)
        
        vectordb = {}
        for pdf_ref in pdf_refs:
            pdf_path = os.path.join(pdf_directory, pdf_ref.name)
            with open(pdf_path, "wb") as f:
                f.write(pdf_ref.getvalue())
            vectordb[pdf_ref.name] = pdf_reader(pdf_path)

        return vectordb

if st.session_state.pdf_refs and not st.session_state.vectordb:
    st.session_state.vectordb = process_pdfs_to_vectordb(st.session_state.pdf_refs)

# Response display section
st.header("Response")
if query and st.session_state.vectordb:
    with st.spinner("Generating response..."):
        combined_response = []
        for pdf_name, db in st.session_state.vectordb.items():
            generated_response = run(db, query)
            if isinstance(generated_response, dict) and 'result' in generated_response:
                response_text = f"**{pdf_name}:** {generated_response['result']}"
                for doc in generated_response['source_documents']:
                    response_text += f"\n\n\nSource document: **{doc['source']}** --> {doc['content']}\n\n"
                combined_response.append(response_text)
            else:
                combined_response.append(f"**{pdf_name}:** Error: Invalid response format")

        formatted_response = "\n\n".join(combined_response)

        st.write("Generated Response:")
        st.markdown(formatted_response)

        st.session_state["user_query_history"].append(query)
        st.session_state["chat_answers_history"].append(formatted_response)

# Display chat history in the main page
if st.session_state["chat_answers_history"]:
    st.header("Chat History")
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_query_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)
