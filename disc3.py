def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m * 1
    else:
        return m + multiply(m, n-1)  # Q1: Warm Up: Recursive Multiplication finished
    
# Q3: Find the Bug
# Find the bug in this recursive function.
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:          # added by myself
        return 1           # added by myself       # Q3: Find the Bug finished
    else:
        return n * skip_mul(n - 2)
    
# Q4: Is Prime
# Write a function is_prime that takes a single argument n and 
# returns True if n is a prime number and False otherwise. 
# Assume n > 1. We implemented this in Discussion 1 iteratively, now time to do it recursively!
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"        # skip
    def check(i):
        "Check whether no number from i up to n evenly divides n."
        if i == n:
            return True
        elif n % i == 0:
            return False
        return check(i + 1)
    return check(2)


# Q5: Recursive Hailstone
# Recall the hailstone function from Homework 1. 
# First, pick a positive integer n as the start. 
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. #偶数就除以2，奇数就乘以三再加1
# Repeat this process until n is 1.             # 重复执行，直到n等于1
# Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)

