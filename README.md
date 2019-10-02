# Functional programming in python

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
function. 

```python
addition = lambda a, b: a + b

print(addition(3, 4)) # returns 7
```

[source](https://kite.com/blog/python/functional-programming/)
