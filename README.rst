======================
cookiecutter-gaelib
======================

Cookiecutter template for a Google App Engine Python library. See https://github.com/audreyr/cookiecutter.

* Free software: BSD license
* Testing setup with `unittest` and `python setup.py test` with Nose_ and NoseGAE_
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/john2x/cookiecutter-gaelib.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist: https://gist.github.com/audreyr/5990987

*"Installing" in a Google App Engine project:*

Since this library will be installed in a GAE project, the user will just need to
place the package somewhere in the GAE project path.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _Nose: http://nose.readthedocs.org/en/latest/
.. _NoseGAE: https://github.com/Trii/NoseGAE
