# Python program to find the frequency of 
# each character in a string

# function definition
# it accepts a string and returns a dictionary 
# which contains the frequency of each chacater
def frequency(text):
    # converting string to lowercase
    text = text.lower()
    # dictionary declaration
    dict = {}
    # traversing the characters
    for char in text:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

# main code
if __name__ == '__main__':
    # inputting the string and printing the frequency
    # of all characters
    user_input = str(input("Enter a string: "))
    print(frequency(user_input))

    user_input = str(input("Enter another string: "))
    print(frequency(user_input))
