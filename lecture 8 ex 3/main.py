file_name1 =()
file_text1 = ()
with open('1.txt', 'r', encoding='utf-8') as f:
    file_name1 = f.name
    file_text1 = f.read()

file_name2 =()
file_text2 = ()
with open('2.txt', 'r', encoding='utf-8') as f:
    file_name2 = f.name
    file_text2 = f.read()

file_name3 =()
file_text3 = ()
with open('3.txt', 'r', encoding='utf-8') as f:
    file_name3 = f.name
    file_text3 = f.read()

with open('final.txt', 'w') as f:
    f.write(file_name2)
    f.writelines('\n')
    f.write(file_text2)
    f.writelines('\n')
    f.write(file_name1)
    f.writelines('\n')
    f.write(file_text1)
    f.writelines('\n')
    f.write(file_name3)
    f.writelines('\n')
    f.write(file_text3)







#count_1 = sum(1 for _ in f)
#print(count_1)
#count_2 = sum(1 for _ in g)
#print(count_2)
#count_3 = sum(1 for _ in h)
#print(count_3)
#file = open('final.txt', 'w', encoding='utf-8')


