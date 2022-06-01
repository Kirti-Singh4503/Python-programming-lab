# list1 - first list of the integers
# lists2 - second list of the integers
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 60, 70]

# printing lists 
print "list1:", list1
print "list2:", list2

# finding and printing differences of the lists
print "Difference elements:"
print (list (set(list1) - set (list2)))
