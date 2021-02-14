# task 1

a = bytes([10, 20, 30, 40])
b = (10, 20, 30)
c = tuple[10,20,30]
d = {10, 20, 30}
f = [10, 20, 30]
g = dict(key1='10', key2='20', key3='30')
my_d = {"key_1": 500, 2: 400, "key_3": True, 4: None}
print(type(a),type(b), type(True), type(None), type(c), type(d), type(f),type(g), type(my_d))

# task 2
def input_arg():
    tpp = input('Введите данные ')
    return tpp
arr = []
j = 0
for i in range(5):
    arr.append(input_arg())
for i in range(int(len(arr) / 2)):
    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    j += 2
print(arr)


# task 3

my_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца  "))
if month ==1 or month == 12 or month == 2:
        print(my_dict.get(1))
elif month == 3 or month == 4 or month == 5:
        print(my_dict.get(2))
elif month == 6 or month == 7 or month == 8:
        print(my_dict.get(3))
elif month == 9 or month == 10 or month == 11:
        print(my_dict[4])
else:
    print("Подсказака: в году 12 месяцев:)")

my_list = ['зима','весна','лето','осень']
month = int(input("Введите номер месяца  "))
if month ==1 or month == 12 or month == 2:
        print(my_list[0])
elif month == 3 or month == 4 or month == 5:
        print(my_list[1])
elif month == 6 or month == 7 or month == 8:
        print(my_list[2])
elif month == 9 or month == 10 or month == 11:
        print(my_list[3])
else:
    print("Подсказака: в году 12 месяцев:)")


# task 4

my_str = input("Введите фразу_")
my_list = []
num = 1
try:
    for i in range(my_str.count(" ") + 1):  # если поставить лишний пробел во фразе (после последнего слова допустим) - выходит ошибка IndexError.Поставила except - ничего получше в голову не пришло
        my_list = my_str.split()
        if len(str(my_list)) <= 10:
            print(f" {num}. {my_list[i]}")
            num += 1
        else:
            print(f" {num}. {my_list[i][0:10]}")
            num += 1
except IndexError as ex:
    print("IndexError")


# task 5
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
el = int((input("Введите цифру. Для завершения введите код: 123456     ")))
while el != 123456:
    for i in range(len(my_list)):
        if my_list[i] == el:
            my_list.insert(i + 1, el)
            break
        elif my_list[0] < el:
            my_list.insert(0, el)
        elif my_list[-1] > el:
            my_list.append(el)
    print(f"текущий рейтинг - {my_list}")
    el = int((input("Введите цифру. (для завершения введите код: 123456)   ")))

# task 6
goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
while True:
    control = input("Для выхода нажмите 'Q', для продолжения нажмите 'Enter', для вывода аналитики нажмите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\nАналитика товаров: \n')
        for key, value in analytics.items():
            print(f'{key}: {value}')
        break
    for f in features.keys():
        ftr = input(f'Введите данные "{f}"')
        features[f] = int(ftr) if (f == 'price' or f == 'quantity') else ftr
        analytics[f].append(features[f])
    goods.append((num, features))