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

With Pip
''''''''

Create a Python virtual environment by executing the following commands::

    git clone https://github.com/Enec0De/pydsadoc.git
    cd pydsadoc
    python -m venv .venv

then activate the virtual environment using one of the following commands::

    # Linux/macOS
    source .venv/bin/activate

    # or Windows
    .venv\Scripts\activate 

For the specific dependencies, you can simply execute either of the following commands::

    # For normal main dependencies
    python -m pip install -U pip
    python -m pip install -e .

    # For optional group dependencies
    python -m pip install -U pip
    python -m pip install -e .[test]


With Poetry
'''''''''''

You can use poetry (advanced Python packaging and dependency management)::

    git clone https://github.com/Enec0De/pydsadoc.git
    cd pydsadoc
    poetry install

For the specific group dependencies::

    # Alternatively, for optional group dependencies
    poetry install -E test
