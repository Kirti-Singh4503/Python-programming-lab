# Python program to find maximum and minimum k elements in tuple 

# Creating a tuple in python 
myTuple = (4, 9, 1, 7, 3, 6, 5, 2)
K = 2

# Finding maximum and minimum k elements in tuple 
sortedColl = sorted(list(myTuple))
vals = tuple(sortedColl[:K] + sortedColl[-K:])

# Printing 
print("Tuple : ", str(myTuple))
print("K maximum and minimum values : ", str(vals))
