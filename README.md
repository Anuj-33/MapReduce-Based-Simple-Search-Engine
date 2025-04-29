# MapReduce-Based Simple Search Engine
This is a lightweight search engine project built in Python.
It processes a BBC News dataset (~40,000 news articles), indexes it using an Inverted Index, and allows users to search for individual words and retrieve relevant documents with a simple snippet and relevance score.

->  Features : 
Text Preprocessing: Lowercasing, removing punctuation, and stopword removal.

Inverted Index Construction: Fast mapping of words to document IDs.

Search Functionality:

Search for one word at a time.

Retrieve matching documents and snippets from the description.

Display a simple relevance score based on word occurrence.

Efficient Performance: Indexes 40k+ rows in just a few seconds.

Clean Modular Code:

data_extraction.py — Main program.

functions.py — Text processing, indexing, and search functions.

# Areas of Improvement (Future Work)
Add support for multi-word search queries.

Improve relevance ranking (e.g., using TF-IDF).

Use stemming (e.g., "running" → "run") to improve search matching.

Add a simple Web UI for searching instead of command-line.

Optimize for larger datasets using database or external indexing libraries.

#  Requirements
Python 3.7+
pandas
nltk

# Author
Anuj Kashyap (https://github.com/Anuj-33)
