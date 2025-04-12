a = input()
print(a)

print(min('pear'))

print(max((1, 2, 3)))

print(max(['나', '그리고', '우리']))

pumpkin = (1, 5, 2, 3, 6)
big = max(pumpkin)
small = min(pumpkin)
print(big, small)

print(sum((1, 2, 3, 4, 5)))
print(len('Triangle'))

my_list = [1, 2, 3, 4, 5]
var1 = sum(my_list)
var2 = len(my_list)
var3 = var1/var2
print(var1, var2, var3)


def my_func(a, b):
    c = 2 * (a + b)
    return c


print(my_func(3, 4))


def greeting():
    # print('bonjour')
    return 'bonjour'


print(greeting())


def my_star(a):
    return '*'*a


print(my_star(7))
