# Python program to order tuples by list

# Creating and printing tuple list and list 
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]

print("The original list is : " + str(tupList))

sortingList = ['l', 'a', 'k', 'e']
print("The sorting list is " + str(sortingList))

# Sorting tuple list based on Sorting list 
valDict = dict()
for key, ele in enumerate(sortingList):
	valDict.setdefault(ele, []).append(key)	
sortedList = sorted(tupList, key = lambda ele: valDict[ele[0]].pop())

# Printing sorted List 
print("The ordered tuple list based on tuple list: " + str(sortedList))
