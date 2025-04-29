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

# Output 
--------------------------------------------------
Enter a word to search (or type 'exit' to quit): india
Document ID: 6747
Snippet: britain left india 75 years ago and the
Relevance Score (Word Count): 2
--------------------------------------------------
Document ID: 361
Snippet: from an airstrike bunker to his mum's relieved hugs, vishnu tells how he and his dog fled ukraine to...
Relevance Score (Word Count): 1
--------------------------------------------------
Document ID: 505
Snippet: with a four-wicket hammering of india in mount maunganui.
Relevance Score (Word Count): 1
--------------------------------------------------
Document ID: 674
Snippet: from blue tokai to sleepy owl, a new wave of homegrown coffee roasters are finding success in india....
Relevance Score (Word Count): 1
--------------------------------------------------
... and so on


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
