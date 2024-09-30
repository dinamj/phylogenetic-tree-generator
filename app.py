import streamlit as st

# Title of the web app
st.title('Phylogenetic Tree Generator')

# Instruction for the user
st.write("This app allows you to upload multiple DNA or protein sequences in FASTA format and generates a phylogenetic tree.")

# File uploader for FASTA files
uploaded_files = st.file_uploader("Please upload FASTA files", type=["fasta"], accept_multiple_files=True)

if uploaded_files:
    st.write("You have uploaded the following files:")
    for file in uploaded_files:
        st.text(file.name)
else:
    st.info("Please upload FASTA files to proceed.")