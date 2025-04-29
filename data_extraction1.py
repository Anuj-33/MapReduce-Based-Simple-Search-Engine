import pandas as pd
import time
from function import preprocess_text, create_inverted_index, search_word

# Load your data (you can replace this with your actual data source)
data = pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\Python program\\Map Reduce\\bbc_news_20220307_20240703.csv")  # Make sure the file path is correct

# Preprocess text in the 'description' column
data['processed_text'] = data['description'].apply(preprocess_text)

# Create the inverted index
start_time = time.time()
inverted_index = create_inverted_index(data)
end_time = time.time()

# Print duration
print(f"Indexing completed in {end_time - start_time} seconds.")

# Print some entries from the inverted index to check
if len(inverted_index) > 0:
    for word, doc_ids in list(inverted_index.items())[:10]:  # Just show the first 10 words for brevity
        print(f"Word: {word}, Document IDs: {doc_ids}")
else:
    print("Inverted index is empty.")

# Search functionality
while True:
    query = input("Enter a word to search (or type 'exit' to quit): ").strip().lower()
    if query == 'exit':
        print("Exiting search.")
        break
    else:
        results = search_word(query, inverted_index, data)
        if isinstance(results, str):  # Error message if word not found
            print(results)
        else:
            for result in results:
                print(f"Document ID: {result['doc_id']}")
                print(f"Snippet: {result['snippet']}")
                print(f"Relevance Score (Word Count): {result['count']}")
                print("-" * 50)


