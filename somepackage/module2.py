def another_function(l1, l2):
    """
    Describe here what this function does,
    its input arguments, and what it returns.
    """
    return l1 + l2


def test_another_function():
    assert another_function([9, 0, 2], [0, 1]) == [9, 0, 2, 0, 1]
    assert another_function('beverly ', 'hills') == 'beverly hills'
