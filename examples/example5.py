from functools import reduce

values = [1, 2, 3, 4, 5, 6]
add = lambda x, y: x + y # values cumulate in x and get updated with y

print(reduce(add, values)) # (((((1+2)+3)+4)+5)+6) = 21 