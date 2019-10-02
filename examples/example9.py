def add(x): 
    def _inner(y): # has access to value of x
        return x + y # last call returns a value
    return _inner # returns function 

print(add(10)(20)) # returns 30
