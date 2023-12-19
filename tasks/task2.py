from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance
import itertools

def calculate_cosine_similarity(sentences):
    # Create a CountVectorizer
    vectorizer = CountVectorizer()

    # Transform the sentences into a sparse matrix of word counts
    sentence_matrix = vectorizer.fit_transform(sentences)

    # Get the array representation for each sentence
    sentence_arrays = sentence_matrix.toarray()

    # Calculate cosine similarity for all pairs of sentences
    similarity_matrix = []
    for pair in itertools.combinations(enumerate(sentence_arrays), 2):
        (i, v1), (j, v2) = pair
        d = distance.cosine(v1, v2)
        similarity_matrix.append((i, j, 1 - d))  # Convert distance to similarity

    return similarity_matrix

# Sample sentences
sentences = [
    "I love programming with Python",
    "Python is a versatile language",
    "Machine learning is fascinating",
    "NumPy makes array manipulation easy",
]

# Calculate cosine similarity for all pairs of sentences
similarity_scores = calculate_cosine_similarity(sentences)

# Display the similarity scores
print("Cosine Similarity Scores:")
for i, j, score in similarity_scores:
    print(f"Similarity between sentences {i+1} and {j+1}: {score:.4f}")
