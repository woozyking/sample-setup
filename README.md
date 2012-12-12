sample-setup
============

Minimal usage of Python package mechanism and distutils.

How To Setup?
=============

Simply run `$ python setup.py insatll`. You'll observe that there is a `build` folder gets populated under the root of this project folder, and the content within will be automatically copied/pasted under system's default Python installation.

To test that this lib has been successfully installed, simply go into Python interactive mode `$ python`, and do `>>> import sample_lib`, if there's no `ImportError` raised, everything's good and *Santa will be here on time*.

The Guts Within
===============

If you dig into /sample_lib, what you'll see is an empty `__init__.py` file. What this file does is to tell Python that this folder is a package, which contains packaged modules m1 and m2. So this makes it possible to do things like `from sample_lib import m1, m2`, `import sample_lib.m1` etc. The setup.py is also very straightforward (just like `__init__.py`, very minimal). In most cases this is more than enough for making your library modules accessible globally. But if you needed some finer or more advanced control, wizardry and/or witchcraft, go ahead and read on [Python Modules and Packages](http://docs.python.org/2/tutorial/modules.html#packages) and [Distributing Python Modules](http://docs.python.org/2/distutils/index.html).
