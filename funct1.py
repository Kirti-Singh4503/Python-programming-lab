# Python program to filter even value 
# using lambda function 

# List of fibonacci values
fibo = [0,1,1,2,3,5,8,13,21,34,55]
print("List of fibonacci values :",fibo)

# filtering even values using lambda function 
evenFibo = list(filter(lambda n:n%2==0,fibo))
print("List of even fibonacci values :",evenFibo)
