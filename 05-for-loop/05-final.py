star = int(input())

for i in range(1, star + 1):
    print("*" * i)


cheeze = []
while True:
    cheeze.append("치즈")
    print("치즈 추가")
    if len(cheeze) == 50:
        print("아아~ 배불러!")
        break