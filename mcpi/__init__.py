# Set some global constants.
#
__version__ = "0.1.0"

# Import the function 'mcpi' from the local module 'mcpi'.
# By putting this line here, the function will be re-exported
# and made available in the package namespace without its module namespace
# as soon as the package, also called 'mcpi', has been imported.
# By using 'import mcpi', the function can then be called by 'mcpi.mcpi(n)'.
#
from .mcpi import mcpi

