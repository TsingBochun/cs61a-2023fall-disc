# Rao Discussion 9: Midterm Review

# Q2: Paths List
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    >>> paths(5, 3) # There is no valid path from x to y
    []
    """
    #if ____________________________________
    #    return ____________________________________
    #elif ____________________________________
    #    return ____________________________________
    #else:
    #    a = ____________________________________
    #    b = ____________________________________
    #    return ____________________________________
    if x > y:
        return []
    elif x == 5:
        return [x]
    else:
        a = paths(x + 1, y)
        b = paths(x * 2, y)
        return [[x] + subpath for subpath in a + b]   # Q2: Paths List FINISHED # 几乎所有正面思考难以解决的问题都可以用递归解决
    
# Q3: Widest Level
def widest_level(t):
    """
    >>> sum([[1], [2]], [])
    [1, 2]
    >>> t = Tree(3, [Tree(1, [Tree(1), Tree(5)]),
    ...              Tree(4, [Tree(9, [Tree(2)])])])
    >>> widest_level(t)
    [1, 5, 9]
    """
    levels = []
    x = [t]
#    while _____________:
#         _____________
#         __________ = sum(_______________________________, [])
#    return max(levels, key=_________________________________)
    #levels = []
    #x = [t]
    while x:
        levels.append([t.label for t in x])
        x = sum([t.branches for t in x], [])       # Q3: Widest Level 完全没看懂
    return max(levels, key=len)


# Q4: Level Mutation Link
def level_mutation_link(t, funcs):
	"""Mutates t using the functions in the linked list funcs.

	>>> t = Tree(1, [Tree(2, [Tree(3)])])
	>>> funcs = Link(lambda x: x + 1, Link(lambda y: y * 5, Link(lambda z: z ** 2)))
	>>> level_mutation_link(t, funcs)
	>>> t
	Tree(2, [Tree(10, [Tree(9)])])
	>>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
	>>> level_mutation_link(t2, funcs)
	>>> t2
	Tree(2, [Tree(100), Tree(15, [Tree(16)])])
	>>> t3 = Tree(1, [Tree(2)])
	>>> level_mutation_link(t3, funcs)
	>>> t3
	Tree(2, [Tree(100)])
	"""
	#if _____________________:
#		return
	#t.label = _____________________
	#remaining = _____________________
	#if __________________ and __________________:
	#	while _____________________:
	#		_____________________
	#		remaining = remaining.rest
	#for b in t.branches:
	#	_____________________
	if funcs is Link.empty:
		return
	t.label = funcs.first(t.label)
	remaining = funcs.rest
	if t.is_leaf() and remaining is not Link.empty:
		while remaining is not Link.empty:
			t.label = remaining.first(t.label)
			remaining = remaining.rest
	for b in t.branches:
		level_mutation_link(b, remaining)     # Q4: Level Mutation Link 大致看懂了

# linked list API
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
        return string + str(self.first) + '>' 
    
# Q5: Shuffle
def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['H', 'D', 'S', 'C']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
    >>> cards[26:30]
    ['7S', '7C', '8H', '8D']
    >>> shuffle(cards)[:12]
    ['AH', '7S', 'AD', '7C', 'AS', '8H', 'AC', '8D', '2H', '8S', '2D', '8C']
    >>> shuffle(shuffle(cards))[:12]
    ['AH', '4D', '7S', '10C', 'AD', '4S', '7C', 'JH', 'AS', '4C', '8H', 'JD']
    >>> cards[:12]  # Should not be changed
    ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    #half = _______________
    #shuffled = []
    #for i in _____________:
    #    _________________
    #    _________________
    #return shuffled   
    half = len(cards) // 2
    shuffled = []
    for i in range(half):
        shuffled.append(cards[i])                # Q5: Shuffle学习：写法真的很精妙，不是看i的奇偶性，而是直接进两个元素
        shuffled.append(cards[half+i])
    return shuffled

# Q7: Pow
def lgk_pow(n,k):
    """Computes n^k.

    >>> lgk_pow(2, 3)
    8
    >>> lgk_pow(4, 2)
    16
    >>> a = lgk_pow(2, 100000) # make sure you have log time
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
         return 1
    elif k % 2 == 0:
         return square(lgk_pow(n, k//2))
    else:
         return n * lgk_pow(n, k-1)
    
# square func
def square(x):
     return x * x         # Q7 finished

# Q8: Yield, Fibonacci!
def fibs(f):
    """Yield all Fibonacci numbers x for which f(x) is a true value.
    >>> odds = fibs(lambda x: x % 2 == 1)
    >>> [next(odds) for i in range(10)]
    [1, 1, 3, 5, 13, 21, 55, 89, 233, 377]
    >>> bigs = fibs(lambda x: x > 20)
    >>> [next(bigs) for i in range(10)]
    [21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
    >>> evens = fibs(lambda x: x % 2 == 0)
    >>> [next(evens) for i in range(10)]
    [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418]
    """
    n, m = 0, 1
#    while _________:
#        if _________:
#            _________
#        n, m = _________, _________
    while True:
        if f(n):
            yield n
        n, m = m, n + m           # Q8: Yield, Fibonacci! 

# Q9: Partitions
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        #yield ____
        yield str(n)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n - m, m):
            yield p + ' + ' + str(m)

    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n, m-1)       # Q9: Partitions 确实没有完全搞明白，当初最早的案例就没搞明白


# Q10: Mint
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2023
    >>> dime = mint.create(Dime)
    >>> dime.year
    2023
    >>> Mint.present_year = 2103  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2023
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2102
    >>> Mint.present_year = 2178     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2023

    def __init__(self):
        self.update()

    # The create method takes a subclass of Coin (not an instance!), 
    # then creates and returns an instance of that class stamped with the mint's year 
    # (which may be different from Mint.present_year if it has not been updated.)
    def create(self, coin):
        "*** YOUR CODE HERE ***"
        return coin(self.year)

        
    #Each Mint instance has a year stamp. 
    #The update method sets the year stamp of the instance to the present_year class attribute of the Mint class
    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.present_year


class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    # A Coin's worth method returns the cents value of the coin plus one extra cent for each year of age beyond 50.
    # A coin's age can be determined by subtracting the coin's year from the present_year class attribute of the Mint class.
    def worth(self):
        "*** YOUR CODE HERE ***"
        return self.cents + max(0, Mint.present_year - self.year - 50)    # Q10: Mint finisehd


class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

    