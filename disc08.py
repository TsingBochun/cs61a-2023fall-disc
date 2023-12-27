# THIS IS DISC08

# linked list ADT
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)     # 断言剩余要么是空表，要么是一个LINK
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ''
            self = self.rest
        return string + str(self.first) + '>'       # Linked List ADT FINISHED and Q1 FINISHED
    
# Q2: Sum Nums
def sum_nums(s):
    """
    Returns the sum of the elements in s.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    result = 0
    if s is Link.empty:
        return ()
    elif s.rest is Link.empty:
        result += s.first
        return result
    else:
        result = s.first + sum_nums(s.rest)
        return result                             # Q2: Sum Nums FINISHED
    

        
        
