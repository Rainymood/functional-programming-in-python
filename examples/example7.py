values = [1, 2, 3, 5, 4, 6]
even = lambda x: x % 2 == 0

print(list(filter(even, values))) # [2, 4, 6]