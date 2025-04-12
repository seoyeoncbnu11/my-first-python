import math
import random
print(random.randrange(0, 2))
print(random.choice(['a', 'e', 'i', 'o', 'u']))
print(random.sample(range(1, 46), 6))

print(math.pi)
print(math.floor(3.1))
print(math.ceil(3.9))

num1 = math.pow(7, 12)
num2 = math.pow(6, 13)

if num1 > num2:
    print('7의 12제곱이 더 큽니다.')
else:
    print('6의 13제곱이 더 큽니다.')
