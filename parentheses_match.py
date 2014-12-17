from ArrayStack import ArrayStack
def parentheses_match(expr):
    """ Return True if all delimiters are properly match; False otherwise."""
    left = '({['        # opening delimiters
    right = ')}]'           # respective closing delims
    
    S = ArrayStack() 
    for c in expr:
        if c in left:
            S.push(c)                # push left delimiter on stack
        elif c in right:
            if S.is_empty():    # nothing to match with
                return False
            if right.index(c) != left.index(S.pop()):
                return False            # mismatched
    return S.is_empty()            # were all symbols matched?
                