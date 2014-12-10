def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]. run @ O(logn)
    
    >>>S = [0,1,2,3,4,5,6,7,8]
    >>>binary_sum(S,0,len(S))
    
    """
    
    if start >= stop: # zero elements in slice
        return 0
    elif start == stop-1: # one element in slice
        return S[start]
    else: # two or more elements in slice
        mid = (start+stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
        