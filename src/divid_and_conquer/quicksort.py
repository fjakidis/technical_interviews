import random

def quicksort(l, r, A):

    if l < r:
        m = split(l, r, A)
        
    quicksort(l, m-1, A)
    quicksort(m + 1, r, A)

def split(l, r, A):
    """ Inputs: 
        - Integer l 
        - Integer r
        - Array A
        Outputs: 
        - Integer j
    """

    array_initial = A
    arr = A

    x  = A[l]
    
    i = l
    j = r 

    print(100*'_')
    print(f"x: {x}")
    print(f"A: {arr}")
    
    while True:

        # First
        print(100*'_')
        while i < len(A) - 1:
            print(f"i: {i} A[i]: {arr[i]}")
            i += 1
            if x <= arr[i]:
                break
        print(f"i: {i} A[i]: {arr[i]}")      
        print()
        if x <= A[i]:
            print(f"x = {x} is less than (or equal to) A[{i}] = {arr[i]}")
        else:
            print(f"The end of the array was reached")
        
        # Second
        print(100*'_')
        while True:
            print(f"j: {j} A[j]: {arr[j]}")
            if x >= arr[j]:
                break 
            j -= 1
        # print(f"j: {j} A[j]: {A[j]}") 
        print()
        if x >= arr[j]:
            print(f"x = {x} is greater than (or equal to) A[{j}] = {arr[j]}")
        else:
            print(f"The start of the array was reached")
        
        # Third
        print(100*'_')
        print(f"i: {i} j: {j}")
        print()
        if i < j:
            # swap(i, j)
            print(f"i = {i} is less than j = {j}")
            print()
            print(arr)
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            print()
            print(arr)
        else:
            # swap(l, j)
            tmp = arr[j]
            arr[j] = arr[l]
            arr[l] = tmp
            print(f"Before: {array_initial}")
            print(f"After:  {arr}")
            print()
            return j

    # End
    print(100*'_')
    print('End of algorithm')

def test():
    
    #test_case_one = [7,8,10,1,2]
    test_array = []
    while len(test_array) < 5:
        num = random.randint(0,10)
        # Make sure not to insert duplicates 
        if num not in test_array:
            test_array.append(num)
    
    l = 0
    r = len(test_array) - 1

    #split(l, r, test_array)
    quicksort(l, r, test_array)


test()