# Python program to find the sum of all elements of the list

# function to find the sum of elements of list
def add(data):
    s=0
    for n in data:
        s=s+n
    return s
    
# List of some fibonacci numbers 
fiboList = [0,1,1,2,3,5,8,13,21,34,55]
print("List of fibonacci numbers :",fiboList)

# calling function to add elements of fibonacci list 
listSum = add(fiboList)
print("The sum of all elements is ",listSum)
