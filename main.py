def print_arry(*arr):
    for x in range(len(arr)): 
        print(arr[x])

def main():
    print("python main function")
    a = [1, 2, 3, 4, 5] 
    print_arry(a)


if __name__ == '__main__':
    main()