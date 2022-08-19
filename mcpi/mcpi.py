# Use the standard facilities to get some random numbers.
#
import random

# This function estimates π by using a simple Monte-Carlo algorithm.
# The parameter provides the number of samples used for the estimation.
#
def mcpi(n):
  result = 0
  for i in range(n):
    x = random.random();
    y = random.random();
    result += (x * x + y * y < 1)
  return 4 * result / n
