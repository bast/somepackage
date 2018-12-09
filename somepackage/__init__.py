from .version import __version__
from .module1 import some_function
from .module2 import another_function

# if somebody does "from somepackage import *", this is what they will
# be able to access:
__all__ = [
    'some_function',
    'another_function',
]
