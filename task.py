from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
# Sample documents
# documents = [
#     "summer is here.",
#     "sky is bright.",
#     "birds are gone.",
#     "nests are empty.",
#     "where is the rain?",
#
# ]
file = open("text file.txt")

# Create a CountVectorizer instance
vectorizer = CountVectorizer()

# Fit the vectorizer to the documents and transform the documents into a BoW representation
X = vectorizer.fit(file)

# Get the vocabulary (unique words) in the documents
vocab = vectorizer.get_feature_names_out()

# Convert the BoW representation to a dense array for easier exploration
# X_dense = X.toarray()

# Display the BoW representation and the vocabulary
print("Bag of Words representation:")
print(X.)
print("\nVocabulary:")
print(vocab)
