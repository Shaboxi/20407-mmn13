import math

# a nice print to the array
# Complexity = O(n)
def print_arry(arr):
    print("")
    for x in range(len(arr)): 
        print(" ",arr[x],end="")
    print("")

# This function extract the max value from a d-ary max heap.
# The max in a d-ary max heap is the root of the heap,
# that means we need to return the value of the first index in the array. 
# before we return this value, we need to run a heapify function that re-orgenize the arry
# since we extracted the root value. 
# Complexity = O(d*log_d(n))
def extract_max(arr, d):
    max = arr[0]
    arr[0] = arr[len(arr)-1]
    del arr[len(arr)-1]
    heapify(arr,0,d)
    return max

# This function get the following parameters:
# arr = array of int's
# i = the index we want to start the process from
# d = the number of sons each parent can have
# The function make sure each d values are between bigger values in the array, 
# which results a n array that answers the definition of d-array max heap
# Complexity = O(d*log_d(n))
def heapify(arr,i,d):
    bigger = i
    for k in range(d * i + 1, d * i + d + 1):
        if d*i+k < len(arr) and arr[d*i+k] > arr[bigger]:
            bigger = k
        else:
            bigger = i
    # if we found that a one of the kids is bigger then the parent
    if i != bigger:
        arr[i] = arr[k]
        heapify(arr,k,d)

# This function adds the value k to the d-arr max heap, 
# and then makes sure the array still keep the rules of an d-arr max heap by running the increase_key function
# Complexity (same as increase_key) O(log_d(n))
def insert(arr,k,d):
    arr.append(k)
    increase_key(arr,len(arr)-1,k,d)

# This function increase the key (value) of an element in the heap
# arr = array of int's
# i = the index we want to start the process from
# k = the value which the index in the arr[i] place will hold
# d = the number of sons each parent can have
# The function compares k and a[i] and then updtes a[i] to be the bigger value,
# and then make sure the array keep the rules of an d-arr max heap
# Complexity O(log_d(n))
def increase_key(arr,i,k,d):
    arr[i] = max(arr[i],k)    
    while i > 0 and arr[get_parent(i,d)] < arr[i]:
        exchange(arr,get_parent(i,d),i)
        i = get_parent(i,d)
        
# return the index of the parent of a specific index in the array 
def get_parent(i,d):
    return math.floor((i-1)/d)        

# switch between two elements in the array
def exchange(arr,k,m):
    temp = arr[k]
    arr[k] = arr[m]
    arr[m] = temp



def main():

    #a = [10, 1, 2, 3, 6, 8, 7, 9] 
    
    # read from file
    inputAsfile = open('input', 'r')
    line = inputAsfile.readlines()
    inputAsfile.close()
    a = line[0].split(",")
    
    # convert strings to int
    for i in range(0, len(a)): 
        a[i] = int(a[i])

    # run some actions on the input

    heapify(a,0,3)
    print_arry(a)
    print_arry(a)    
    increase_key(a,7,12,3)
    print_arry(a)
    insert(a,15,3)
    print_arry(a)
    
    for k in range(0,len(a)):
        extract_max(a,3)
        heapify(a,0,3)
        print_arry(a)







if __name__ == '__main__':
    main()