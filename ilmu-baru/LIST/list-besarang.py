from itertools import chain
a = [[14, 24, 34], [4, 5, 6], [12, 34, 56]]
b = list(chain(*a))
print(a.sort())
print(a)
print(*a)
print(b)
