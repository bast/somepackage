def my_add(argument1, argument2):
    """
    Describe here what this function does,
    its input parameters, and what it returns.

    In this example the function adds the two input
    arguments.
    """
    result = argument1 + argument2
    return result


def test_my_add():
    assert my_add([9, 0, 2], [0, 1]) == [9, 0, 2, 0, 1]
    assert my_add('beverly ', 'hills') == 'beverly hills'
