# addition
phrase = ['banana', 'apple', 'mango', 'strawberry', 'cherry']
print("\t1 addition")
phrase += ["watermelon"]
print(phrase)

# multiplying
print("\t2 multiplying")
print(phrase * 2)

# indexing
print('\t3 indexing')
print(phrase[0], phrase[-1])

# slicing
print('\t4 slicing')
print("0:2\n", phrase[:2], '\n2:5\n', phrase[2:5], '\nall with step 2\n',  phrase[::2])

# sorting
print('\t5 sort words in the string alphabetically')

# option 1
phrase.sort()
print('sort 1\n', phrase)

# option 2
s2 = sorted(phrase)
print('sort 2\n', s2)


