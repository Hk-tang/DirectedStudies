# Directed Studies Exploratory Repository

## Collaborators

* Henry Tang (hktang@ualberta.ca)

# Overview

This repository contains the Python scripts used for the directed studies course, CMPUT 605.
It contains my exploration and implementation of Latent Sematic Analysis (LSA), and k-clustering.
The `data` directory contains the code examples of the 5 libraries documentation.
The `results` directory contains the elbow method graph of clustering the different examples for each document for each library.
The clustering is of the code examples within **one** page of documentation of a library.
i.e., for each document (page) in a library's documentation I perform clustering on the code examples of that document.

The `k_cluster/manual.py` and `k_cluster/text_k.py` file are not used to generate the clusters analyzed in the project.
They were used for me to gain a better understanding of k-clustering.
`k_cluster/text_k.py` is the implementation of k-clustering that is used to generate clusters from code examples in documentation.
`LSA/lsa.py` is my implementation of using LSA on the documentation code examples.

The `Ground Truth.xlsx` file contains the data from the manual analysis of the 5 libraries.

## Input
The input should be at least one directory **in the data directory** containing at least one subdirectory with **at least 6 text** files. e.g., 
```
data/
    library_1/
        document_1/
            example_1.txt
            example_2.txt
            ...
            example_6.txt
        document_2/
            example_1.txt
            example_2.txt
            ...
            example_6.txt
        ...
    library_2/
        ...
```
Each text file should be non-empty, containing at least a one line code example.

Example input files are provided in the `data` directory

## Installation and execution

1. Clone the repository and create a virtual environment
    ```
    python3 -m venv venv
    ```
2. Start the virtual environment and install project dependencies
    ```
    source venv/bin/activate # For Unix
    venv\Scripts\activate.bat # For Windows
    pip install -r requirements.txt
   ```
3. Run the program from the project root directory
    ```
   python k_cluster/text_k.py
   ```

## Results
Results are outputted to the results directory under that library's name and document.
They are PNG images of the graph generated from the elbow method.

## Resources
These are the resources that I used for this repository.

* https://benalexkeen.com/k-means-clustering-in-python/

* https://www.kaggle.com/dfoly1/k-means-clustering-from-scratch

* https://towardsdatascience.com/k-means-clustering-8e1e64c1561c

* https://towardsdatascience.com/clustering-metrics-better-than-the-elbow-method-6926e1f723a6
