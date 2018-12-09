from .module2 import another_function


def some_function():
    """
    Describe here what this function does,
    its input parameters, and what it returns.
    """
    t = _shout('hey ho -')
    return another_function(t, t)


def test_some_function():
    assert some_function() == 'HEY HO -HEY HO -'


# the underscore signals that this function is not to be used outside this
# module
def _shout(text):
    """
    Describe here what this function does,
    its input parameters, and what it returns.

    In this example the function converts the input string
    to uppercase.
    """
    result = text.upper()
    return result


def test_shout():
    assert _shout('have a nice day') == 'HAVE A NICE DAY'
