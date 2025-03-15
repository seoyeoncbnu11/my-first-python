i = 0
while True:
    print('knock')
    if i >= 3:
        break
    i = i + 1

for i in range(1, 5):
    if i == 3:
        break
    print(i)
print('i가 3입니다.')

i = 1
while True:
    print(i, '월 1만 원을 입금했습니다.')
    if i == 12:
        print('입금 완료! 12만원을 수령하세요!')
        break
    i = i + 1

count = 4
while True:
    count = count - 1
    print(count)
    if count == 1:
        print('땡!')
    break

i = 1
sum = 0
while True:
    sum = sum + i
    print(i, sum)
    if i > 9:
        break
    i = i + 1
print(sum)