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
    #t = it
    t = iter(it)
    #lst.append(next(it))
    lst.append(next(t))
    while True:
        #tmp = next(it)
        tmp = next(t)
        yield tmp - lst[-1]
        lst.append(tmp)         # ⭐️写到这里    # Q4: What's the Difference? FINISHED # RuntimeError: generator raised StopIteration



#Q5: Primes Generator
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    "*** YOUR CODE HERE ***"
    iterator = reversed(range(2, n+1))
    for term in iterator:
        if is_prime(term):
            yield term

    
