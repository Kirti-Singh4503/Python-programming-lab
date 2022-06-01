# Creating an empty Dictionary 
Record = {} 
print("The Dictionary is: ") 
print(Record) 

# Adding one element at a time
Record[0] = 'Amit'
Record[1] = 'Kumar'
Record[2] = 21
Record[3] = 'Delhi'
print("\nNow, the Dictionary is: ") 
print(Record) 

# adding multiple values to a key
Record['marks'] = 69, 70, 58
print("\nNow, the Dictionary is: ") 
print(Record) 

# Updating an existing Key's Value 
Record[2] = 23
print("\nNow, the Dictionary is: ") 
print(Record) 

# Adding Nested Key value
Record[4] = {'Nested' :{'Name' : 'Shivang', 'Age' : 24}} 
print("\nNow, the Dictionary is: ") 
print(Record) 
