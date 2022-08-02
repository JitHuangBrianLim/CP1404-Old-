import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
Smallest number that could have been seen for line 1 is 5, while the largest is 20.

Smallest number that could have been seen for line 2 is 3, while the largest is 9.

Smallest number that could have been seen for line 3 is 2.5, while the largest is 5.5.
"""

print(random.randint(1, 100))   # random number between 1 and 100 inclusive
