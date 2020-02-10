.. image:: https://travis-ci.org/bast/somepackage.svg?branch=master
   :target: https://travis-ci.org/bast/somepackage/builds
.. image:: https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg
   :target: ../master/LICENSE


Somepackage
===========

Show how to structure a Python project.

Inspired by https://github.com/kennethreitz/samplemod.


Great resources
===============

- https://manikos.github.io/a-tour-on-python-packaging
- https://docs.python-guide.org/writing/structure/
- http://veekaybee.github.io/2017/09/26/python-packaging/
- https://github.com/audreyr/cookiecutter-pypackage
- https://medium.com/@jonas.r.kemper/understanding-best-practice-python-tooling-by-comparing-popular-project-templates-6eba49229106


Recommendations
===============

Please browse this blog post for a good summary of recommendatios and templates: https://medium.com/@jonas.r.kemper/understanding-best-practice-python-tooling-by-comparing-popular-project-templates-6eba49229106


Python 2 or 3?
--------------

- Develop your code under Python 3, test it for both Python 2 and Python 3
  but consider Python 3 to be the default today.


Split your code into packages, modules, and functions
-----------------------------------------------------

- All code should be inside some function (except perhaps ``if __name__ == '__main__':``).
- Split long functions into smaller functions.
- If you need to scroll through a function over several screens, it is probably too long.
- Functions should do one thing and one thing only.
- Hide internals with underscores.
- Organize related functions into modules.
- If modules grow too large, split them.
- Import from other modules under ``somepackage/`` using ``from .somemodule import something``.
- Do file I/O on the "outside" of your code, not deep inside.


Classes vs. functions
---------------------

- Do not overuse classes.
- Prefer immutable data structures.
- Prefer pure functions.


Naming
------

- Give the subdirectory the same name as your package.
- Before you name your package, check that the name is not taken on https://pypi.org
  (you may want to upload your package to PyPI one day).


Interfaces
----------

- In ``somepackage/__init__.py`` define what should be visible to the outside.
- Use https://semver.org.


Testing
-------

- Test all non-trivial code. I recommend to use https://pytest.org.
- Use Travis CI: https://docs.travis-ci.com/user/languages/python/.


Dependency management
---------------------

- Package dependencies for developers should be listed in ``requirements.txt``.
- Alternatively, consider using http://pipenv.readthedocs.io.
- Package dependencies for users of your code (who will probably install via pip) should be listed in ``setup.py``.


Code style
----------

- Follow PEP8: https://www.python.org/dev/peps/pep-0008/
- Use ``pycodestyle`` to automatically check for PEP8.


Type checking
-------------

- Consider using type hints: https://docs.python.org/3/library/typing.html
- Consider using http://mypy-lang.org.
- Consider verifying type annotations at runtime: https://github.com/RussBaz/enforce


Share your package
------------------

- Choose a license and add a LICENSE file.
- Share your package on PyPI. For this you can follow https://github.com/bast/pypi-howto.


Documentation
-------------

I used to recommend reStructuredText for READMEs in contrast to Markdown but
PyPI no longer requires reStructuredText. You can use Markdown as noted on
https://pypi.org/help/ under "How can I upload a project description in a
different format?".

Example shown here: https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py


Suggestions? Corrections? Pull requests?
----------------------------------------

Yes please!
