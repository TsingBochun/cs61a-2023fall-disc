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
            string += str(self.first) + ' '
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
    

# Q3: Remove All
def remove_all(link, value):
    """Removes all nodes in link that contain value. The first element of
    link is never equal to value.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    remain = link.rest
    if remain is Link.empty:
        return 
    else:
        while True:
            if remain.first == value:
                remain = remain.rest
            else:
                link.rest = remain
                remain = 
        #    link.rest = remain.rest
            link.rest = remain.rest
            print(link)   # only for debug
    #remove_all(link.rest, value)
    #if link.rest is link.empty:
    #    return
    #elif link.rest.first == value:
    #    link.rest = link.rest.rest
    #remove_all(link, value)


# Q5: Make Circular

    
    


        
        
