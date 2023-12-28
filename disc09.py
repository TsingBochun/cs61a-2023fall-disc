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
    
    