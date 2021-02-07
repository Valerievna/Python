# task 1

a = 6
b = 4.5
print(float(a ** b))
print(a % b)

k = input("введите число1 ")
k = int(k)
e = input("введите число2 ")
e = int(e)
r = input("введите число3 ")
r = float(r)
print(k+e+r)


# task 2

import datetime


def convert(n):
    return str(datetime.timedelta(seconds=n))


n = int(input("введите секунды "))
print(convert(n))


def convert(sec):
    return str(datetime.timedelta(seconds=sec))


sec = int(input("введите секунды "))
minutes = sec // 60
hours = minutes // 60
print(convert(sec))


# task 3
n = input('Введите число_ ')
m = int(2 * n)
k = int(3 * n)
n = int(n)
print("результат: ", m + k + n)


# task 4
i = int(input("введите число больше 10_"))
H = []
while i > 10:
    H.append(i % 10)
    i = i // 10
r = max(H)
print(r)


# task 5
revenue = int(input("введите сумму выручки_"))
cost = int(input("введите сумму затрат_"))
if revenue > cost:
    qt = int(input("введите численность сотрудников_"))
    profit = (revenue - cost)/ revenue * 100
    cr = (revenue - cost) / qt
    print('Прибыль составляет', '%.2f' % profit , '% прибыль на одого сотрудника: ', '%.2f' % cr, 'руб.')
else:
    print('Убыток ', revenue - cost, 'руб. Не отчаивайся, всё получится :)')


# task 6
l = 9
al = 2
count = 0
while al < l:
    count += 1
    print(count, 'день', '%.2f' % al, 'км')
    al = al + al * 10/100
    rt = al > l
print(count, 'день', '%.2f' % al, 'км')

