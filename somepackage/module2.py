def another_function(argument1, argument2):
    """
    Describe here what this function does,
    its input parameters, and what it returns.
    """
    return argument1 + argument2


def test_another_function():
    assert another_function([9, 0, 2], [0, 1]) == [9, 0, 2, 0, 1]
    assert another_function('beverly ', 'hills') == 'beverly hills'
