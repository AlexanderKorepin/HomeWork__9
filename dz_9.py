import numpy as np
# Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.
def zadacha_1():
    numbers = np.random.randint(0, 10, (10))
    print(numbers)
    num = len(np.unique(numbers))
    print(f'Количество уникальных элементов в списке : {num}')

#-----------------------------------------------------------
# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.
def zadacha_2():
    array = np.random.randint(0, 2, (5, 5))
    print(array)
    if len(array) != len(set(map(tuple, array))):
        print("В массиве есть одинаковые строки")
    else:
        print("В массиве нет одинаковых строк")

#---------------------------------------------------------
# Задача 3. Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.
def zadacha_3():
    array = np.random.randint(1, 10, (5, 5))
    result = np.diagonal(array)
    print(f'Матрица:\n{array}')
    max_index = np.unravel_index(np.argmax(array), array.shape)
    min_index = np.unravel_index(np.argmin(array), array.shape)
    print("Индекс максимального элемента:", max_index)
    print("Индекс минимального элемента:", min_index)
    print(f'Диагональ матрицы:\n{result}')


