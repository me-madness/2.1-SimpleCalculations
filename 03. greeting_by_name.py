#first way
name = input('name = ')
print('Hello, ' + name + '!')


#second way 
name = input()
print('Hello, ', end='')
print(name, end='!')

#third way
name = input()
print(f'Hello, {name} !')