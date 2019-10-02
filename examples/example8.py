people = [
    {
        'first_name': 'Bruce',
        'last_name': 'Wayne'
    },
    {
        'first_name': 'Joker',
        'last_name': ''
    }
]

joined_names = ','.join(list(map(lambda d: d['first_name'], people)))

print(joined_names) # Bruce,Joker