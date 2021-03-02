# task 1

file = open("text.txt", 'w', encoding ='UTF-8')
text = input("Ввод_ \n")
while text:
    file.write(text)
    text = input("Ввод_ \n")
    if not text:
        break
file.close()
file = open("text.txt", 'r', encoding ='UTF-8')
print(file.read())


# task 2

fl = open("task2.txt", 'r')
print(fl.read())
fl = open("task2.txt", 'r')
m = fl.readlines()
print(f'Количество строк в файле - {len(m)}')
fl = open("task2.txt", 'r')
fl = fl.read()
b = str(fl.splitlines())
print(f'Общее количество слов - {len(b.split())}')
fl = open("task2.txt", 'r')
my_list = fl.read().split('\n')
cnt = 0
for i in my_list:
    i = i.split()
    f= len(i)
    cnt +=1
    if f > 0:
        print(f'Количество слов {cnt} - й строки: {f}')
    else:
        break


# task 3

with open('task3.txt', 'r') as my_file:
    sal = []
    lower = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           lower.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20000 {lower}, средний оклад {sum(map(int, sal)) / len(sal)}') # подсмоттрела решение, можно на разборе дз поподробнее рассказать про "map'


# task 4

d = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('task4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ')
        new_file.append(d[i[0]] + " " + i[1])
        print(new_file)

with open('file_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)


# task 5

with open('task5.txt', 'w+') as file_5:
    line = input('Введите цифры через пробел \n')
    file_5.writelines(line)
    numb = line.split()
    print(sum(map(int, numb)))

# task 6

table = {}
with open('task6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        table[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {table}')


# task 7
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('task7.txt', 'r') as file:
    for line in file:
        name, form, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')