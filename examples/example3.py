names = ['Bert', 'Johnannes', 'Zoe']
print(sorted(names, key=len)) # ['Zoe', 'Bert', 'Johnannes']
print(sorted(names, key=lambda name: name[-1])) # ['Zoe', 'Johnannes', 'Bert']
