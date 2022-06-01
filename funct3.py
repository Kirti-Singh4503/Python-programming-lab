# Function to replace characters
# Here, we will assign the string 
# in which replacement will be done
# and, two characters to be replaced 
# with each other

def replace(s,c1,c2):
    # Lambda expression to replace c1 with c2
    # and c2 with c1
     new = map(lambda x: x if (x!=c1 and x!=c2) else \
                c1 if (x==c2) else c2,s)
  
     # Now, join each character without space
     # to print the resultant string
     print (''.join(new))
  
# main function
if __name__ == "__main__":
    str = 'Heool wlrod!'
    ch1 = 'l'
    ch2 = 'o'
    
    print("Original string is:", str)
    print("Characters to replace:", ch1, "and", ch2)
    
    print("String after replacement:")
    replace(str,ch1,ch2)
