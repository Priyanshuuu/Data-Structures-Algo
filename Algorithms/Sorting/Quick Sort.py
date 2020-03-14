def Quick(A):
    sort(A,0,len(A)-1)
    return A

def sort(A,low,up):
    if low>=up:
        return
    p = partition(A,low,up)
    sort(A,low,p-1)
    sort(A,p+1,up)
    
def partition(A,low,up):
    piv = A[low]
    i, j = low+1, up
    while i<=j:
        while A[i]<piv and i<up:
            i += 1
        while A[j]>piv: 
            j -= 1
        if i<j:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
            j -= 1
        else:
            break
    A[low], A[j] = A[j], piv
    return j
 
print(Quick([4, 3, 5, 1, 6, 2]))
 
