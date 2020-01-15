def print_arry(arr):
    for x in range(len(arr)): 
        print(arr[x], end="")

# This function extract the max value from a d-ary max heap.
# The max in a d-ary max heap is the root of the heap,
# that means we need to return the value of the first index in the array. 
# before we return this value, we need to run a heapify function that re-orgenize the arry
# since we extracted the root value. 
def extract_max(arr, d):
    max = arr[0]
    arr[0] = arr[-1]
    del arr[-1] 
    heapify(arr,0,d)
    return max

# 
def heapify(arr,i,d):
    bigger = i
    for k in range(0 , d-1):
        if d*i+k < len(arr) and arr[d*i+k] > arr[bigger]:
            bigger = k
        else:
            bigger = i
    # if we found that a one of the kids is bigger then the parent
    if i != bigger:
        arr[i] = arr[k]
        heapify(arr,k,d)


def main():
    print("python main function")
    a = [10, 1, 2, 3, 6, 8, 7, 9] 
    #a = [8,1,2,3,6] 
    print_arry(a)
    
    for k in range(0,len(a)):
        print("")
        extract_max(a,3)
        print_arry(a)
                





if __name__ == '__main__':
    main()