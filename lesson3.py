# task 1
def div(*args):

    try:
        arg1 = int(input("введите число  "))
        arg2 = int(input("введите число  "))
        res = arg1 / arg2
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    return res
print(div())

# task 2
def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
name = input('enter name ')
surname = input('enter surname ')
year = input('enter year ')
city = input('enter city ')
email = input('enter email ')
telephone = input('input telephone ')
print(my_func(surname=surname, name=name, year=year, city=city, email=email,
              telephone=telephone))
# task 3
def my_func1():
    agg = []
    a = int(input('enter number '))
    agg.append(a)
    b = int(input('enter number '))
    agg.append(b)
    c = int(input('enter number '))
    agg.append(c)
    return(max(agg))
print(my_func1())
# task 4
'''
Способ № 1
Решение задачи с помощью возведения в степень
'''

def my_func2(x, y):
    acc = x**y
    return acc
x = int(input('enter x '))
y = int(input('enter y '))
print(my_func2(x,y))

'''
Способ № 2
Решение задачи с помощью цикла
'''

def my_func2(x, y):
    ex = 1
    while ex < y:
        ass = x*x
        ex += 1
    return ass
x = int(input('enter x '))
y = int(input('enter y '))
print(my_func2(x,y))

# task 5

def sum_number():
    sum_res = 0
    ex = True
    while ex == True:
        number = input('Введите несколько чисел через пробел. Для выхода нажмите W - ').split( )

        res = 0
        for i in range(len(number)):
            if number[i] == 'w' or number[i] == 'W':
                ex = False
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Сумма равно {sum_res}')
    print(f'программа завершина')
sum_number()

# task 6

def int_func(*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()

def text_func():
    ls = []
    text = input('Input text: ').split()
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)
print(text_func())
