import streamlit as st
from Bio import AlignIO, Phylo
from Bio.Align import MultipleSeqAlignment
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import matplotlib.pyplot as plt
from io import StringIO
import os

# Title of the web app
st.title('Phylogenetic Tree Generator')

# Instruction for the user
st.write("This app allows you to upload multiple DNA or protein sequences in FASTA format and generates a phylogenetic tree.")

# File uploader for FASTA files
uploaded_files = st.file_uploader("Please upload a minimum of four FASTA files to ensure a reliable phylogenetic tree", type=["fasta"], accept_multiple_files=True)

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

            # Create the alignment object
            alignment = MultipleSeqAlignment(aligned_sequences)

            # Display the alignment
            st.write("### Sequence Alignment")
            st.text(str(alignment)[:1000])  # Limit to first 1000 characters

            # Perform distance calculation using the identity model
            calculator = DistanceCalculator('identity')
            distance_matrix = calculator.get_distance(alignment)

            # Construct the phylogenetic tree using the Neighbor-Joining method
            constructor = DistanceTreeConstructor(calculator, method="nj")
            tree = constructor.build_tree(alignment)

            # Display the phylogenetic tree graphically
            st.write("### Phylogenetic Tree")
            fig = plt.figure(figsize=(10, 5))
            ax = fig.add_subplot(1, 1, 1)
            Phylo.draw(tree, axes=ax)  # Explicitly assign axes to avoid missing visualization
            st.pyplot(fig)

            # Option to download the tree in Newick format
            tree_io = StringIO()
            Phylo.write(tree, tree_io, "newick")
            tree_io.seek(0)

            # Allow user to download the Newick format of the tree
            st.download_button("Download Tree in Newick Format", data=tree_io.getvalue(), file_name="phylogenetic_tree.newick")

        except Exception as e:
            st.error(f"Error running Clustal Omega: {e}")
else:
    st.info("Please upload FASTA files to generate a phylogenetic tree.")