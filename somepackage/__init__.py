from .version import version_info, __version__
from .module1 import some_function
from .module2 import another_function

# if somebody does "from somepackage import *", this is what they will
# be able to access:
__all__ = [
    'version_info',
    'some_function',
    'another_function',
]
