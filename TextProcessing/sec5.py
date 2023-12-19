from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance

li = [
    "i love apple.",
    "i love apple."
]
vextorizer = CountVectorizer()
v = vextorizer.fit_transform(li)
v1 = v.toarray()[0]
v2 = v.toarray()[1]
d = distance.cosine(v1, v2)
print(f"{d*100}%")

# todo any num of sentences