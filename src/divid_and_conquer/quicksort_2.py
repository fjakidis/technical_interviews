def split(l, r, A):
    
    x = A[l]
    i = l 
    j = r 
    
    while i < len(A) - 1:
        i += 1
        if x <= A[i]:
            break
    
    while True:
        if x >= A[j]:
            break
        j -= 1
    
    if i < j:
        tmp = A[j]
        A[j] = A[i]
        A[i] = tmp

    
    