a = 'once'
print(a[-1])

b = ['t', 'w', 'i', 'c', 'e']
print(b[:3])
print(b[:])

bag1 = ['은', '은', '은', '은', '은', '은', '은', '은',
        '은', '은', '은', '은', '은', '은', '다이아몬드', '은']
jewel1 = bag1[-2]

bag2 = ['은', '은', '은', '은', '은', '은', '은', '은', '은', '은', '은',
        '은', '은', '금', '금', '금', '금', '금', '금', '금', '금', '금']
jewel2 = bag2[-8:]
print('두더지 가방 안의 가장 비싼 보석', jewel1)
print('두더지 가방 안의 금빛 보석들', jewel2)
