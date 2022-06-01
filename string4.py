# Python program to check if a string is 
# palindrome or not

# function to check palindrome string
def isPalindrome(string):
  result = True
  str_len = len(string)
  half_len= int(str_len/2)

  for i in range(0, half_len):
    # you need to check only half of the string
    if string[i] != string[str_len-i-1]:
      result = False
    break
  
  return result 

# Main code
x = "Google"
if isPalindrome(x):
  print(x,"is a palindrome string")
else:
  print(x,"is not a palindrome string")  

x = "ABCDCBA"
if isPalindrome(x):
  print(x,"is a palindrome string")
else:
  print(x,"is not a palindrome string")

x = "RADAR"
if isPalindrome(x):
  print(x,"is a palindrome string")
else:
  print(x,"is not a palindrome string") 
