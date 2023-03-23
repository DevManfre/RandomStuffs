from CollatzConjecture import CollatzConjecture

# 1 int param -> give the number sequence
print(CollatzConjecture(9))

# 2 int param -> give the numbers sequence of the range
print(CollatzConjecture(1,11))

# 1 tuple param -> give the numbers sequence of the range but with tuple or list
A = CollatzConjecture([1,11])
print(A)

# fullDescription -> get all sequence and the elapsed time (for testing)
print(A.fullDescription())