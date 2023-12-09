# This is practise of disc04.

# Q1: Count Stair Ways
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    result = 0
    if n == 1:         # 台阶只有一个，那么一次迈一个，只有一种方法
        result =  1
    elif n == 2:
        result =  2      # 台阶有两个，那么一次迈一个迈两次，或者一次迈两个，有两种方法
    else:
        #result_last1 = count_stair_ways(n-1) + 1       # 计算当最后一步只需迈一个的时候方法
        # result_last2 = count_stair_ways(n-2)       # 计算当最后一步为两个台阶的方法
        #result = result_last2 + count_stair_ways(2)
        result = count_stair_ways(n-2) + count_stair_ways(n-1)     # Q2 Count Stair Ways: FINISHED
    return result
    # 问题本身相当于将n按照不大于2进行分割有多少种方法：           # Q1: Count Stair Ways skip


# Q2: Count K
def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        for step in range(1, k + 1):
            total += count_k(n - step, k)
        return total          # Q2: Count K SKIP       # Q2: Count K: answer  

# Q3: Insect Combinatorics
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    # 假设到达目标地左侧（m，n-1）位置后（用了N1种放啊），只需要再往右移动一下，或者到达目标地下面（m-1， n）（用了N2种方法）后再往上移动一下
    if m == 1 or n == 1:
        return 1       # 只有一种方法，如果初始位置在目的地的左侧或者下方，也是本题的基底。
    else:
        return paths(m - 1, n) + paths(m, n - 1)        # Q3: Insect Combinatorics finish
    
# Q4: Max Product
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    "*** YOUR CODE HERE ***"
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))
        # OR
    #    return max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))      q4 ANSWER

# Q5: Flatten
def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6]
    >>> deep                                # input list is unchanged
    [1, [[2], 3], 4, [5, 6]]
    >>> very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
    >>> flatten(very_deep)
    ['m', 'i', 'n', 'm', 'e', 'w', 't', 'a', 't', 'i', 'o', 'n', 's']
    """
    "*** YOUR CODE HERE ***"
    # 假设除最后一个元素外的前面所欲元素用该函数已经完成，只需判断最后一个元素是否为list，或者说不需要判断，直接用list改造成list就行
    #list = []
    #if len(s) == 1:
    #    list = s
    #else:
    #    list = flatten( s[ 0: len(s) - 2 ] ) + flatten ( s[ len(s) - 1 ] )
    #return list

    lst = []
    for elem in s:
        if type(elem) == list:
            lst += flatten(elem)
        else:
            lst += [elem]
    return lst               # 这个解法并不是递归   # Q5: Flatten 非递归解法



    
    
