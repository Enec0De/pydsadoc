PyDSADoc
========

This is a Python project focused on implementing Data Structure and Algorithms.
The primary goal of this project is to learn DSA concepts through hands-on
implementation.  In other words, it is a practice-oriented learning project.

The Project uses Python 3.9.  To ensure version consistency, it is recommended
to create a corresponding virtual environment.  All reference materials will be
based on the `Python 3.9.24 documentation <https://docs.python.org/3.9/>`__.

It should be noted that this version has reached its End-Of-Life (EOL). For
actual production environment, please use a more recent version. For the sake
of practice, the project may includes some files that are unnecessary for
simple projects, such as the ``.pyi`` stub files.


Getting started
---------------

Create a Python virtual environment by executing the following commands::

    git clone https://github.com/Enec0De/pydsadoc.git
    cd pydsadoc
    python -m venv .venv

then activate the virtual environment::

    # Linux/macOS
    source .venv/bin/activate

    # or Windows
    .venv\Scripts\activate 

For the dependencies, you can simply execute the following command::

    # With normal dependencies
    python -m pip install -U pip
    python -m pip install -e .[test]

    # or with optional dependencies
    python -m pip install -U pip
    python -m pip install -e .[test]

or you can use poetry (advanced Python packaging and dependency management)::

    # With normal dependencies
    poetry install

    # or with optional dependencies
    poetry install -E test
