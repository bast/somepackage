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
- Test all non-trivial code.
- Organize related functions into modules.
- Split long functions into smaller functions.
- Hide internals with underscores.
- Give the subdirectory the same name as your package.
- Before you name your package, check that the name is not taken on https://pypi.org.
- Use ``pycodestyle``.


Suggestions? Corrections? Pull requests?
----------------------------------------

Yes please!
