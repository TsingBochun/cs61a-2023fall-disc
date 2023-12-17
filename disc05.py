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
    return False        # Q3: Less Than FINISHED

# Q5: Height
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***" # TREE的问题先SKIP还有递归

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree is a leaf. (i.e. It has no branches.)"""
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


