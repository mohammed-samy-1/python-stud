from sklearn.feature_extraction.text import CountVectorizer
#open and read file 
f = open("poem.txt", "r")
text = f.read()
text.lstrip()
text.rstrip()
print(text)
lines = text.split('\n')
print(lines)

# Create a Vectorizer Object
vectorizer = CountVectorizer()

vectorizer.fit(lines)

# Printing the identified Unique words along with their indices
print("Vocabulary: ", vectorizer.vocabulary_)

# Encode the Document
vector = vectorizer.transform(lines)

# Summarizing the Encoded Texts
print("Encoded Document is:")
print(vector.toarray())
