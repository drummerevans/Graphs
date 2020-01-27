names = ['James', 'Matt', 'Oscar', 'Matthew']

select = input('Please input a name you would like to find: ')

for name in names:
    if name == select:
        print(name)

