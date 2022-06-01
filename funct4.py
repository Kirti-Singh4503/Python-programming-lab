# Function: ArrayIntersection
# the function will accept two arrays
# and, will find the intersection

def ArrayIntersection(a1, a2):
     # Here, the lambda expression will filter
     # the element e list a2 where e
     # also exists in a1
     result = list(filter(lambda x: x in a1, a2)) 
     print ("Intersection : ",result)
  
# Main function
if __name__ == "__main__":
    # Two arrays 
    array1 = [11, 10, 22, 20, 35, 67]
    array2 = [22, 30, 35, 11]
    
    # function call to find intersection
    ArrayIntersection(array1, array2)
