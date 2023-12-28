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