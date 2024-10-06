## About The Project

This web application allows users to generate and visualize phylogenetic trees from DNA or protein sequences uploaded in FASTA format. Using Streamlit for the interface and Biopython for sequence analysis, the app performs multiple sequence alignment with Clustal Omega and constructs phylogenetic trees using the Neighbor-Joining method. Users can upload multiple sequences, view both the alignment and tree visualization, and download the tree in Newick format.

You can try the live version of the app [here](https://phylogenetic-tree-generator-pcr4uy8lnctpzxgua5mxce.streamlit.app/)

Example FASTA files are provided in the ´example_files´ folder for testing purposes. You can use these files to see how the app works. Please ensure Clustal Omega is installed and available in your system's PATH. You can download it from the [official Clustal Omega website](http://www.clustal.org/omega/).

## Built With

- Python
- Python Libraries, such as Biopython, Matplotlib
- Clustal Omega
- Streamlit
- Git



## Installation

**Requirements:**

- Python (tested on Version [3.11.8](https://www.python.org/downloads/release/python-3118/))
- [Clustal Omega](http://www.clustal.org/omega/) (installed and available in system PATH)
- (only tested on Windows)


**Installation steps:**

1. Clone the repository and navigate to the project directory.

2. Install the required libraries by running the following command in your terminal:
```
pip install -r requirements.txt
```

3. Ensure Clustal Omega is installed and available in your system's PATH. You can download it from the [official Clustal Omega website](http://www.clustal.org/omega/).



## Usage

After the successfully completing all steps in the `Installation`, you can run the Streamlit app with the following command in your terminal:
```
streamlit run app.py
```

Upload at least four DNA or protein sequences in FASTA format to generate a phylogenetic tree. The app will perform sequence alignment and visualize the phylogenetic tree within the web interface. You can also download the tree in Newick format for further analysis.




## Contact

LinkedIn: Dina Mahdi-Joest [https://www.linkedin.com/in/dina-mahdi-joest-340204220/](https://www.linkedin.com/in/dina-mahdi-joest-340204220/)

GitHub: https://github.com/dinamj

E-Mail: dinamahdijoest@gmail.com