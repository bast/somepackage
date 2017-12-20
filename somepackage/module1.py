from .module2 import another_function


def some_function():
    """
    Describe here what this function does,
    its input arguments, and what it returns.
    """
    t = _internal_function(' fun')
    return another_function(t, t)


def test_some_function():
    assert some_function() == 'something funsomething fun'


# the underscore signals that this function is not to be called outside
def _internal_function(s):
    """
    Describe here what this function does,
    its input arguments, and what it returns.
    """
    return 'something' + s


def test_internal_function():
    assert _internal_function(' fun') == 'something fun'
    assert _internal_function(' to do') == 'something to do'
    assert _internal_function('') == 'something'
