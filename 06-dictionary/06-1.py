my_list = [1,2,3,4,5]
my_list.pop(0)

print(my_list)

my_list.pop()
print(my_list)

my_list = [1,2,3,4,5]
print(my_list.remove(1))

my_seq = [2,2,2,4,4]
print(my_seq.count(2))

my_list = [1,2,2,3,3,3]
var = my_list.count(3)
print(var)

my_list.pop(1) #[1,2,3,3,3]
my_list.pop(2) 
my_list.pop(2)
print(my_list)

my_str = 'ialikeayou'
print(my_str.split('a'))

my_str = '1 2 3 4 5'
print(my_str.split())

element = 'Na,Mg,Al,Si'
print(element.split(','))

dessert = ['Coffee', 'Donut']
print('&'.join(dessert))

dessert = ['ice', 'cream']
print(''.join(dessert))

my_list = ['Seeing', 'is', 'Believing']
var = ' '.join(my_list)
print(var)

lyrics = '바람이,분다,바람이,불어,연평,바다에,어허어얼싸,돈바람,분다,얼싸,좋네,아,좋네,군밤이요,에헤라,생률,밤이로구나,달도,밝다,달도,밝아,우주,강산에,어허어얼싸,저,달이,밝아,얼싸,좋네,아,좋네,군밤이요,에헤라,생률,밤이로구나'
lyric_list = lyrics.split(',')
print(lyric_list[16])