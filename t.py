# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# Step 1: Tokenization - Split the documents into words
words = [doc.split() for doc in documents]

# Step 2: Create a vocabulary (a set of unique words)
vocabulary = set(word for doc in words for word in doc)

# Step 3: Create a dictionary to map words to indices
word_to_index = {word: i for i, word in enumerate(vocabulary)}

# Step 4: Initialize a matrix with zeros (rows represent documents, columns represent words)
num_documents = len(documents)
num_words = len(vocabulary)
bow_matrix = [[0] * num_words for _ in range(num_documents)]

# Step 5: Populate the matrix with word counts
for doc_index, doc in enumerate(words):
    for word in doc:
        word_index = word_to_index[word]
        bow_matrix[doc_index][word_index] += 1

# Step 6: Display the Bag of Words matrix and the vocabulary
for doc_index, document in enumerate(bow_matrix):
    print(f"Document {doc_index + 1} BoW representation:")
    print(document)

print("\nVocabulary:")
print(list(vocabulary))
