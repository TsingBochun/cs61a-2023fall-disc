# Q1: Extending Rationals
from math import gcd

def make_rat(num, den):
    """Creates a rational number, given a numerator and denominator.

    >>> a = make_rat(2, 4)
    >>> numer(a)
    1
    >>> denom(a)
    2
    """
    "*** YOUR CODE HERE ***"
    return [num, den]

def numer(rat):
    """Extracts the numerator from a rational number."""
    "*** YOUR CODE HERE ***"
    return rat[0]

def denom(rat):
    """Extracts the denominator from a rational number."""
    "*** YOUR CODE HERE ***"
    return rat[1]           # Q1: Extending Rationals FINISHED



# Q2: Divide
def div_rat(x, y):
    """The quotient of rationals x/y.
    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> numer(c)
    9
    >>> denom(c)
    20
    """
    "*** YOUR CODE HERE ***"
    result = [0, 0]
    # 分子是，X的分子，乘以Y的分母
    result[0] = numer(x) * denom(y)
    # 分母是，X的分母，乘以Y的分子
    result[1] = denom(x) * numer(y)
    return result                    # Q2: Divide FINISHED


# Q3: Less Than
def lt_rat(x, y):
    """Returns True iff x < y as rational numbers; else False.
    >>> a, b = make_rat(6, 7), make_rat(12, 16)
    >>> lt_rat(a, b)
    False
    >>> lt_rat(b, a)
    True
    >>> lt_rat(a, b)
    False
    >>> a, b = make_rat(-6, 7), make_rat(-12, 16)
    >>> lt_rat(a, b)
    True
    >>> lt_rat(b, a)
    False
    >>> lt_rat(a, a)
    False
    """
    "*** YOUR CODE HERE ***"
    x_0 = denom(x)    # x 的分母
    x_1 = numer(x)    # x 的分子
    y_0 = denom(y)    # y 的分母
    y_1 = numer(y)    # y 的分子
    result = (x_1 * y_0 - x_0 * y_1) / x_0 * y_0
    if result < 0:
        return True
    return False
