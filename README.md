# Functional programming in python

![](https://miro.medium.com/max/180/0*l0y9Olr-DI61Lqr5.png)

## Example 1

Because everything in Python is an object, we can assign functions to variables
as done in `examples/example1.py`

```python
def add(a, b):
    return a + b

plus = add

plus(3, 4)  # returns 7
```

[source](https://kite.com/blog/python/functional-programming/)

## Example 2

Using the protected keyword `lambda` we can create functions in a declarative
way. This keyword comes from [lambda
calculus](https://www.inf.fu-berlin.de/lehre/WS03/alpi/lambda.pdf) and has its
roots in formal mathematics. Simply put, when you see lambda think of anonymous
function. In `examples/example2.py` we create an anonymous/lambda function and
assign it to `addition`. 

```python
addition = lambda a, b: a + b

addition(3, 4) # returns 7
```

[source](https://kite.com/blog/python/functional-programming/)

## Example 3

An application of lambda functions can be found in `examples/example3.py`. We
have a short list of three names and we sort this. The `key` argument takes in a
function upon which we can sort. By creating the `lambda` function called `last`
we iterate over the items of the list and take the last letter. If you pay close
attention you see that the second list is sorted in alphabetical order based on
the last character. 

```python
names = ['Bert', 'Johnannes', 'Zoe']

sorted(names, key=len) # ['Zoe', 'Bert', 'Johnannes']
sorted(names, key=lambda last: last[-1]) # ['Zoe', 'Johnannes', 'Bert']
```

[source](https://kite.com/blog/python/functional-programming/)

## Example 4

Simply put, **map applies a function every item in a sequence.** Map itself
returns a `map object`, hence the need for `list()`. If you ever find yourself
trying to loop over a list and want to do *something* with every element of the
list maybe you need a `map()`. Take a look at the following example found in `examples/example5.py`. 

```python
values = [1, 2, 3, 4, 5, 6]
multiply_by_2 = lambda x: x * 2

list(map(multiply_by_2, values)) # [2, 4, 6, 8, 10, 12]
```

[source](https://kite.com/blog/python/functional-programming/)

## Example 5

The function `reduce` does somewhat the opposite of `map`. Simply put, **reduce applies a function of two arguments iteratively, reducing the list to a single value.** An example makes it clear immediately what reduce does. Check out the following example in `examples/example5.py`. It should be noted that Guido van Rossum hates `reduce` as evident from [this blog (2005)](https://www.artima.com/weblogs/viewpost.jsp?thread=98196)

```python
from functools import reduce

values = [1, 2, 3, 4, 5, 6]
add = lambda x, y: x + y # values cumulate in x and get updated with y

reduce(add, values) # (((((1+2)+3)+4)+5)+6) = 21 
```

[source](https://docs.python.org/3/library/functools.html#functools.reduce)

## Example 6

One of the most common uses for `map` can be found in `examples/example6.py` in combination with Pandas. First, we create a DataFrame with two column and then create a third one by multiplying each value by two. Note that in this case `df['col3'] = df['col2] * 2` would also suffice.

```python
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [10, 20, 30]})
#    col1  col2
# 0     1    10
# 1     2    20
# 2     3    30

df['col3'] = list(map(lambda x: x * 2, df['col2']))
#    col1  col2  col3
# 0     1    10    20
# 1     2    20    40
# 2     3    30    60
```

## Example 7

**Filter takes in a function and a list and returns the elements of the list where the function evaluates as true.** For example, consider `examples/example7.py`. Note that often `filter()` can be written more nicely and concisely as a list comprehension. 

```python
values = [1, 2, 3, 5, 4, 6]
even = lambda x: x % 2 == 0

list(filter(even, values)) # [2, 4, 6]
```

This is equivalent to

```python
[x for x in values if x % 2 == 0] # [2, 4, 6]
```

[source](https://stackabuse.com/functional-programming-in-python/)