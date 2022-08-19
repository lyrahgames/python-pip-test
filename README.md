# Python Test Package for `pip`

This is a small test repository which shows the most basic setup and code for a Python package that may be installed by `pip`.

## Usage

Clone the repository from GitHub using `git` and change into its directory.

    git clone https://github.com/lyrahgames/python-pip-test.git
    cd python-pip-test/

Run the tests and make sure they fail.
Obviously, the test package has not been installed up to this point.

    python tests/run.py

Install the package given in the local directory for the current user and Python version by using `pip`.

    python -m pip install .

Run the tests again.
Now, they should be successful.

    python tests/run.py

Alternatively, open the Python command prompt in a *different* working directory and test it yourself.

```python
import mcpi
mcpi.mcpi(100000)
```

To uninstall the locally installed package, run the following.

    python -m pip uninstall mcpi


## Setup

The test package is called `mcpi` for Monte-Carlo Pi and its purpose is to estimate π by one of the simplest Monte-Carlo algorithms.
All the code needed for this task can be found in the module `mcpi/mcpi.py`.
It will not be further explained here.
The directory structure for the whole package is given in the following scheme.

```
Repository
├── .gitignore
├── README.md
├── mcpi              # Python Package Directory
│   ├── __init__.py   # Python Package Creator
│   └── mcpi.py
├── setup.py          # Setup File to Enable 'pip' Functionality
└── tests
    └── run.py        # Tests whether installation was successful.

```

The tests were put in an extra directory 'tests' not only because it provides better organization.
Putting a script in the main directory enables it to see the local package without it being installed.
This would make it possible to run all the tests without any issues even if the package has not been installed.

The file `setup.py` is needed for `pip` to be able to install the given package.
It provides some metadata for the package by using the standard setup tools.

For the design of the package itself, we only re-export the function `mcpi` provided by the local module `mcpi.py` in the package creator `__init__.py` to make its call possible directly from the package's namespace.

# References

