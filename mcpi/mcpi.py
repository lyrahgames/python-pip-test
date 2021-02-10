import random

def mcpi(n):
  result = 0
  for i in range(n):
    x = random.random();
    y = random.random();
    result += (x * x + y * y < 1)
  return 4 * result / n