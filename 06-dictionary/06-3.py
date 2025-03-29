person = {'name': 'Alice', 'age': 10}
print(person['name'])
person['hometown'] = 'Seoul'
print(person)
del person['name']
print(person)

my_dict = {'사과': 'apple', '바나나': 'banana', '당근': 'carrot'}
my_var = my_dict['사과']
del my_dict['당근']
my_dict['체리'] = 'Cherry'
print(my_dict)

my_dict = {1: 'One', 1: 'Yi'}
print(my_dict)
