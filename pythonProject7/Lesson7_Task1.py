"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
 (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        my_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.list_1)):
            for j in range(len(self.list_2[i])):
                my_matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matrix]))

my_matrix_exp = Matrix([[4, 1, 1],[0, 7, 6],[1, 0, 3]], [[0, 5, 7],[0, 1, 3],[2, 2, 6]])

print(my_matrix_exp.__add__())
