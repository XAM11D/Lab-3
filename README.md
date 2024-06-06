# Lab-3
Лабораторна робота 3: Робота з функціями та списками у Python

Мета роботи
Мета цієї лабораторної роботи - вивчення роботи з функціями та списками у Python, виконання різних операцій над елементами списків, рядками та числовими даними. Очікувані результати включають написання та тестування функцій, що виконують ці завдання.

Опис завдання
Завдання 1: Модифікувати список, знайти мінімальний та максимальний елементи, а також довжину списку.
Завдання 2: Розрахувати загальну вартість товарів, середню ціну та знайти товар з найбільшим запасом.
Завдання 3: Створити два списки чисел: перший від 1 до 25, другий від -25 до -1.
Завдання 4: Порахувати кількість символів 'a' у рядку.
Завдання 5: Замінити слово "GOOD" на "NICE" у рядку та підрахувати кількість слів.
Завдання 6: Знайти суму елементів списку.
Завдання 7: Знайти числа, що діляться на 7 та 5 у заданому списку.

Виконання роботи
Завдання 1:
def task1(my_list):
    my_list.insert(1, -5)
    min_element = min(my_list)
    max_element = max(my_list)
    my_list.insert(2, [1, 2, 3])
    my_list.append("Прізвище ім'я")
    list_length = len(my_list)
    print("my list", my_list)
    print("min element", min_element)
    print("max element", max_element)
    print("list length", list_length)
    return my_list, min_element, max_element, list_length
    
# Приклад використання:
my_list = [10, 20, 30]
result = task1(my_list)

Завдання 2:
def task2(A, B, C):
    total_cost = sum([quantity * price for quantity, price in zip(B, C)])
    average_price = sum(C) / len(C)
    max_stocked_index = B.index(max(B))
    most_stocked_item = A[max_stocked_index]
    return total_cost, average_price, most_stocked_item

# Приклад використання:
items = ["item1", "item2", "item3"]
quantities = [10, 5, 8]
prices = [100, 200, 150]
result = task2(items, quantities, prices)

Завдання 3:
def task3():
    A1 = [i for i in range(1, 26)]
    A2 = [i for i in range(-25, 0)]
    return A1, A2

# Приклад використання:
A1, A2 = task3()

Завдання 4:
def task4(my_string):
    count_a = my_string.count('a')
    return count_a

# Приклад використання:
result = task4("banana")

Завдання 5:
def task5(my_string):
    modified_str = my_string.replace("GOOD", "NICE")
    word_count = len(my_string.split())
    return modified_str, word_count

# Приклад використання:
result = task5("This is a GOOD example.")

Завдання 6:
def task6():
    list = [1, 2, 3, 4, 5]
    total_sum = sum(list)
    return total_sum

# Приклад використання:
result = task6()

Завдання 7:
def task7(my_list):
    result = [num for num in my_list if num % 7 == 0 and num % 5 == 0]
    return result

# Приклад використання:
my_list = [35, 70, 15, 40, 55]
result = task7(my_list)


Приклади виводу програми:

Завдання 1: ([10, -5, [1, 2, 3], 20, 30, "Прізвище ім'я"], -5, 30, 6)
Завдання 2: (3200, 150.0, "item1")
Завдання 3: ([1, 2, 3, ..., 25], [-25, -24, -23, ..., -1])
Завдання 4: 3
Завдання 5: ("This is a NICE example.", 5)
Завдання 6: 15
Завдання 7: [35, 70]

Інструкції з запуску
Вимоги до середовища: Python 3.x
