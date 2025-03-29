num = int(input())
if 1 <= num <= 9:
    print('한 자리 숫자입니다.')
elif 10 <= num <= 99:
    print('두 자리 숫자입니다.')
else:
    print('세 자리 숫자입니다.')

score = int(input())
if score >= 88:
    print('A+')
elif score >= 77:
    print('A0')
elif score == 0:
    print('F')
else:
    print('B+')
