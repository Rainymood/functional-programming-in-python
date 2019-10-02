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

Simply put **map applies a function every item in a sequence.** Map itself
returns a `map object`, hence the need for `list()`. If you ever find yourself
trying to loop over a list and want to do *something* with every element of the
list maybe you need a `map()`. 

```python
values = [1, 2, 3, 4, 5, 6]
multiply_by_2 = lambda x: x * 2

list(map(multiply_by_2, values)) # [2, 4, 6, 8, 10, 12]
```

[source](https://kite.com/blog/python/functional-programming/)
