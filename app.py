import streamlit as st
from Bio import AlignIO
from Bio.Align.Applications import ClustalOmegaCommandline
import os

# Title of the web app
st.title('Phylogenetic Tree Generator')

# Instruction for the user
st.write("This app allows you to upload multiple DNA or protein sequences in FASTA format and generates a phylogenetic tree.")

# File uploader for FASTA files
uploaded_files = st.file_uploader("Please upload FASTA files", type=["fasta"], accept_multiple_files=True)

# Path to Clustal Omega executable
clustalomega_exe = r"C:\Users\Dinam\Downloads\clustalo\clustalo.exe"  # Replace with your actual Clustal Omega path

if uploaded_files:
    # Save the uploaded sequences to a temporary file
    with open("input_sequences.fasta", "w") as f:
        for file in uploaded_files:
            f.write(file.getvalue().decode("utf-8"))
    
    # Check if Clustal Omega executable exists
    if not os.path.exists(clustalomega_exe):
        st.error("Clustal Omega executable not found. Please install Clustal Omega and provide the correct path.")
    else:
        # Run Clustal Omega for multiple sequence alignment
        output_file = "aligned_sequences.fasta"
        clustalomega_cline = ClustalOmegaCommandline(infile="input_sequences.fasta", outfile=output_file, verbose=True, auto=True, force=True)

        # Execute Clustal Omega and catch any errors
        try:
            stdout, stderr = clustalomega_cline()

            # Read the aligned sequences
            aligned_sequences = AlignIO.read(output_file, "fasta")

            # Display the alignment
            st.write("### Sequence Alignment")
            st.text(str(aligned_sequences)[:1000])  # Limit to first 1000 characters

        except Exception as e:
            st.error(f"Error running Clustal Omega: {e}")
else:
    st.info("Please upload FASTA files to proceed.")