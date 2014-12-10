def linear_sum(S, n):
    """ Return the sum of the first n numbers of sequence S. This algorithm
    takes O(n) time.
    >>>S = [4,3,6,2,8]
    >>>linear_sum(S, 5)
    23
    """
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
        
