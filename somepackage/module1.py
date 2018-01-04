from .module2 import another_function


def some_function():
    """
    Describe here what this function does,
    its input parameters, and what it returns.
    """
    t = _internal_function('hey ho -')
    return another_function(t, t)


def test_some_function():
    assert some_function() == 'HEY HO -HEY HO -'


# the underscore signals that this function is not to be used outside
def _internal_function(parameter):
    """
    Describe here what this function does,
    its input parameters, and what it returns.
    """
    return parameter.upper()


def test_internal_function():
    assert _internal_function('shouting') == 'SHOUTING'
