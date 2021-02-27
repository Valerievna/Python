# task 1
from sys import argv

def res(argv):
    time = int()
    salary = int()
    bonus = int()
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')

print(res(*argv))


# task 2
my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Новый список {my_new_list}')


# task 3
print([el for el in range (20,241) if el % 20 == 0 or el % 21 == 0])


# task 4
list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in list  if list.count(el) < 2]
print(new_list)


# task 5
from functools import reduce

def my_func(el, el_l):
    return el * el_l

print({reduce(my_func, [el for el in range(99, 1001)])})


# task 6
from itertools import count
limit = 0
for el in count(int(input("Введите число_"))):
    limit += 1
    if limit < 1000:
        print(el)
    else:
        break
print("Цикл окончен")


from itertools import cycle
limit = 0
for el in cycle([input(f"Перечислите любимые пирожки_ \n")]):
    limit += 1
    if limit < 10:
        print(el)
    else:
        break
print("Цикл окончен")


# task 7
def fact(n):
    cnt = 1
    for i in range(1, n+1):
        cnt *= i
        yield cnt

n = int(input("Укажите факториал какого числа Вы хотели бы узнать?\n"))
for x in fact(n):
    print(x)