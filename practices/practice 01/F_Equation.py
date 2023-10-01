"""Calculates the sum of the series:
  (X0 - 1) + (X2) + (X4) + (X6) + ............... + (XN)

  Args:
    x: The base number.
    n: The number of terms in the series.

  Returns:
    The sum of the series.
  """

def calculate_sum(x, n):
  
  sum = 0
  for i in range(0, n + 1, 2):
    sum += x ** i - 1

  return sum

x, n = map(int, input().split())
sum = calculate_sum(x, n)
print(sum)