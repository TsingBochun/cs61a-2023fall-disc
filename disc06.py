# THIS IS DISC06

# Q3: Filter-Iter
def filter_iter(iterable, f):
    """
    Generates elements of iterable for which f returns True.
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    for element in iterable:
        if f(element):
            yield element     # Q3: Filter-Iter FINISHED

# Q4: What's the Difference?
def differences(it):
    """ 
    Yields the differences between successive terms of iterable it.

    >>> d = differences(iter([5, 2, -100, 103]))
    >>> [next(d) for _ in range(3)]
    [-3, -102, 203]
    >>> list(differences([1]))
    []
    """
    "*** YOUR CODE HERE ***"
    lst = []
    t = it
    #lst.append(next(it))
    lst.append(next(t))
    while True:
        #tmp = next(it)
        tmp = next(t)
        yield tmp - lst[-1]
        lst.append(tmp)         # ⭐️写到这里
