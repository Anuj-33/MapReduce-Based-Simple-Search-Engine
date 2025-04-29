import re
import nltk
from nltk.corpus import stopwords
from collections import defaultdict

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    if isinstance(text, str):
        # Lowercase
        text = text.lower()
        # Remove non-alphabetic characters
        text = re.sub(r'[^a-z\s]', '', text)
        # Tokenize
        words = text.split()
        # Remove stopwords
        words = [word for word in words if word not in stop_words]
        return words
    else:
        return []

def create_inverted_index(data):
    inverted_index = defaultdict(list)
    total_rows = len(data)

    for idx, row in data.iterrows():
        if isinstance(row['processed_text'], list):
            for word in row['processed_text']:
                if idx not in inverted_index[word]:
                    inverted_index[word].append(idx)
        else:
            print(f"Error: processed_text in row {idx} is not a list.")

        if idx % 1000 == 0:
            print(f"Processing row {idx} of {total_rows}...")

    return inverted_index

def get_snippet(description, word):
    words = description.split()
    if word in words:
        index = words.index(word)
        start = max(0, index - 5)
        end = min(len(words), index + 6)
        snippet = ' '.join(words[start:end])
    else:
        snippet = description[:100] + "..."  # First 100 characters
    return snippet

def search_word(word, inverted_index, data):
    if word not in inverted_index:
        return f"The word '{word}' was not found in any document."

    doc_ids = inverted_index[word]
    results = []

    for doc_id in doc_ids:
        description = data.loc[doc_id, 'description']
        snippet = get_snippet(description.lower(), word)
        word_count = data.loc[doc_id, 'processed_text'].count(word)

        results.append({
            'doc_id': doc_id,
            'snippet': snippet,
            'count': word_count
        })

    results = sorted(results, key=lambda x: x['count'], reverse=True)
    return results
