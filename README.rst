.. image:: https://travis-ci.org/bast/somepackage.svg?branch=master
   :target: https://travis-ci.org/bast/somepackage/builds
.. image:: https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg
   :target: ../master/LICENSE


Somepackage
===========

Show how to structure a Python project.

Inspired by https://github.com/kennethreitz/samplemod.


Recommendations
---------------

- In ``somepackage/__init__.py`` define what should be visible to the outside.
- Test all non-trivial code. I recommend to use https://pytest.org.
- All code should be inside some function (except perhaps ``if __name__ == '__main__':``).
- Split long functions into smaller functions.
- If you need to scroll through a function over several screens, it is probably too long.
- Hide internals with underscores.
- Organize related functions into modules.
- If modules grow too large, split them.
- Import from other modules using ``from .somemodule import something``
- Do file I/O on the "outside" of your code, not deep inside.
- Give the subdirectory the same name as your package.
- Before you name your package, check that the name is not taken on https://pypi.org.
- Share your package on PyPI. For this you can follow https://github.com/bast/pypi-howto.
- Use ``pycodestyle``.
- Use Travis CI: https://docs.travis-ci.com/user/languages/python/.
- Use https://semver.org.
- Add a license and a LICENSE file.
- Use RST for your README (to make it easier for https://pypi.org).


Suggestions? Corrections? Pull requests?
----------------------------------------

Yes please!
