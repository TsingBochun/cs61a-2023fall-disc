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
        result = count_stair_ways(n-2) + count_stair_ways(n-1) 
    return result
    # 问题本身相当于将n按照不大于2进行分割有多少种方法：           # Q1: Count Stair Ways skip

    
    
