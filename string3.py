# Function to split into words
# and print words with its length

def splitString (str):
	# split the string by spaces
	str = str.split (' ')
	# iterate words in string
	for words in str:
		print words," (", len (words), ")"


# Main code 
# declare string and assign value 
str = "Hello World How are you?"

# call the function
splitString(str)
