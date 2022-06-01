#Checks if the given number falls within the given range:
def tips_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start
print(tips_range(2, 4, 6))
print(tips_range(4, 8))
print(tips_range(1, 3, 5))
print(tips_range(1, 3))
