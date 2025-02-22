import random

# i = int(input())

# if i >= 90:
#     print('A')
# elif i >= 75:
#     print('B')

# x = int(input())
# if x % 2 == 0:
#     print('2의 배수입니다.')
# elif x % 3 == 0:
#     print('3의 배수입니다.')

ans = random.randint(1,50)

while True:
    num = int(input())
    if num > ans :
        print('그 수보다 작아요.')
    elif num < ans :
        print('그 수보다 커요.')
    else:
        print('정답!')
        break
