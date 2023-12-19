import numpy as np
documents = [
    "hello it's mohammed samy",
    "welcome mohammed samy",
    "hello it's ahmed",
    "mohammed samy ali mohammed"
]
l = list({j for i in documents for j in i.split()})
l = sorted(l)
arr = np.zeros((len(documents), len(l)))
print(arr)
for i in range(len(documents)):
    for j in documents[i].split():
        arr[i, l.index(j)] += 1
print(l)
print(arr)

