# from PyQt6 import uic
# from PyQt6.QtWidgets import QApplication
#
# Form, Window = uic.loadUiType("dialog.ui")
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# first = 0
# second = 0
# third = 0
# fourth = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i < j:
#             if i < n - 1 - j:
#                 first += matrix[i][j]
#             elif i > n - 1 - j:
#                 second += matrix[i][j]
#         elif i > j:
#             if i < n - 1 - j:
#                 fourth += matrix[i][j]
#             elif i > n - 1 - j:
#                 third += matrix[i][j]
# print(f'Верхняя четверть: {first}\nПравая четверть: {second}\nНижняя четверть: {third}\nЛевая четверть: {fourth}')


# n = int(input())
# m = int(input())
# matrix = [[0]*m for _ in range(n)]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         matrix[i][j] = i * j
# for i in range(n):
#     print(*[str(_).ljust(3) for _ in matrix[i]])


# n = int(input())
# m = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# max_ = -100
# for i in matrix:
#     if max(i) > max_:
#         max_ = max(i)
# a = 0
# for _ in matrix:
#     try:
#         print(a, _.index(max_), sep=' ')
#         break
#     except ValueError:
#         a += 1
#         continue

# n = int(input())
# m = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# s = input().split(' ')
# for _ in matrix:
#     _[int(s[0])], _[int(s[1])] = _[int(s[1])], _[int(s[0])]
#     print(*_)

# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[j][i]:
#             print('NO')
#             quit()
# print('YES')

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (i == j) or (i == n - 1 - j):
#             print(matrix[n - 1 - i][j], end=' ')
#         else:
#             print(matrix[i][j], end=' ')
#     print()

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# for i in range(n // 2):
#     matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
# for _ in matrix:
#     print(*_)

# n = int(input())
# matrix = [input().split() for _ in range(n)]
# for j in range(n):
#     for i in range(n - 1, -1, -1):
#         print(matrix[i][j], end=' ')
#     print()

# s = input()
# x, y = 'abcdefgh'.index(s[0]), 8 - int(s[1])
# matrix = [['.' for j in range(8)] for i in range(8)]
# matrix[y][x] = 'N'
# for i in range(8):
#     for j in range(8):
#         if (y - i) * (x - j) in [-2, 2]:
#             matrix[i][j] = "*"
# for i in matrix:
#     print(*i)

# n = int(input())
# matrix = [[int(i) for i in input().split()] for j in range(n)]
# a = 0
# b = []
# for i in matrix:
#     b += i
# for i in range(1, n**2 + 1):
#     if i in b:
#         continue
#     else:
#         print('NO')
#         quit()
# for j in range(len(matrix[0])):
#     if sum(matrix[j]) != sum(matrix[0]):
#         print('NO')
#         quit()
#     for q in range(len(matrix)):
#         a += matrix[q][j]
#     if a != sum(matrix[0]):
#         print('NO')
#         quit()
#     else:
#         a = 0
#         continue
# for q in range(len(matrix)):
#     a += matrix[q][q] + matrix[q][len(matrix)-q-1]
# print('YES' if a / 2 == sum(matrix[0]) else 'NO')

# n, m = input().split()
# n, m = int(n), int(m)
# matrix = [['.' for j in range(m)] for i in range(n)]
# for _ in range(n):
#     for i in range(len(matrix[0])):
#         if _ % 2 == 0 and i % 2 != 0:
#             matrix[_][i] = '*'
#         elif _ % 2 != 0 and i % 2 == 0:
#             matrix[_][i] = '*'
# for i in matrix:
#     print(*i)

# n = int(input())
# matrix = [[2] * n for _ in range(n)]
# for i in range(n):
#     for _ in range(n):
#         matrix[i][n - i - 1] = 1
# for i in range(n):
#     for j in range(n - i - 1):
#         matrix[i][j] = 0
# for i in matrix:
#     print(*i)

# n, m = input().split()
# n, m = int(n), int(m)
# matrix = [[i for i in range(m)] for _ in range(n)]
# a = 1
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = str(j * n + i + 1)
# for _ in matrix:
#     for i in _:
#         print(i.ljust(3), end='')
#     print()

# n = int(input())
# matrix = [['0']*n for _ in range(n)]
# for i in range(n):
#     matrix[i][i] = '1'
#     matrix[i][n-i-1] = '1'
# for i in matrix:
#     for _ in i:
#         print(_.ljust(3), end='')
#     print()

# n = int(input())
# matrix = [['0'] * n for _ in range(n)]
# for i in range(n):
#     matrix[i][i] = '1'
#     matrix[i][n - i - 1] = '1'
#     for j in range(n):
#         if i < j and i < n - 1 - j:
#             matrix[i][j] = '1'
#         elif i > j and i > n - 1 - j:
#             matrix[i][j] = '1'
# for i in matrix:
#     for _ in i:
#         print(_.ljust(3), end='')
#     print()


# n, m = input().split()
# n, m = int(n), int(m)
# s = 0
# matrix = [['0']*m for _ in range(n)]
# a = [i for i in range(1, m + 1)]
# for i in range(n):
#     for _ in range(m):
#         matrix[i][_] = a[s % m]
#         s += 1
# print(matrix)

# print(' '.join('Сборка'))
# print('Сборка'.swapcase())

# n, m = map(int, input().split())
# matrix = [['0'] * m for _ in range(int(n))]
# j = 1
# for i in range(n):
#     for _ in range(m):
#         matrix[i][_] = str(j).ljust(3)
#         j += 1
#     if i % 2 != 0:
#         matrix[i].reverse()
# for i in matrix:
#     print(*i)

# n, m = map(int, input().split())
# matrix = [['0'] * m for _ in range(int(n))]
# s, k = 1, 0
# while s != n * m + 1:
#     for i in range(n):
#         for j in range(m):
#             if i + j == k:
#                 matrix[i][j] = str(s).ljust(3)
#                 s += 1
#     k += 1
# for i in matrix:
#     print(*i)

#
# n, m = map(int, input().split())
# matrix = [[0] * int(m) for i in range(n)]
# a, b, c = 0, 0, 1
# rows = n - 1
# cols = m - 1
#
# while a <= cols and b <= rows:
#     for i in range(a, cols + 1):
#         matrix[a][i] = str(c).ljust(3)
#         c += 1
#     b += 1
#     for i in range(b, rows + 1):
#         matrix[i][cols] = str(c).ljust(3)
#         c += 1
#     cols -= 1
#     if b <= rows:
#         for i in range(cols, a-1, -1):
#             matrix[rows][i] = str(c).ljust(3)
#             c += 1
#         rows -= 1
#     if a <= cols:
#         for i in range(rows, b-1, -1):
#             matrix[i][a] = str(c).ljust(3)
#             c += 1
#         a += 1
# for i in matrix:
#     print(*i)

# n, m = map(int, input().split())
# matrix_1 = [input().split() for i in range(n)]
# input()
# matrix_2 = [input().split() for j in range(n)]
# matrix_3 = [[0] * int(m) for q in range(n)]
# for i in range(n):
#     for _ in range(m):
#         matrix_3[i][_] = eval(matrix_1[i][_]) + eval(matrix_2[i][_])
# for i in matrix_3:
#     print(*i)

# import numpy as np
# n, m = map(int, input().split())
# matrix_1 = np.array([[int(j) for j in input().split()] for i in range(n)])
# input()
# k, r = map(int, input().split())
# matrix_2 = np.array([[int(j) for j in input().split()] for q in range(k)])
# matrix_3 = matrix_1.dot(matrix_2)
# for i in matrix_3:
#     print(*i)

# import numpy as np
# n = int(input())
# matrix = np.array([[int(j) for j in input().split()] for i in range(n)])
# m = int(input())
# for i in np.linalg.matrix_power(matrix, m):
#     print(*i)

# n, m = input().split(), int(input())
# a = []
# for i in range(m):
#     a.append(n[i::m])
# print(a)

# n, a = int(input()), []
# matrix = [[int(_) for _ in input().split()] for i in range(n)]
# for i in range(len(matrix)):
#     for j in range(n):
#         if i >= n - 1 - j:
#             a.append(matrix[i][j])
# print(max(a))

# import numpy as np
#
# n = int(input())
# matrix = np.array([[int(_) for _ in input().split()] for i in range(n)])
# for i in matrix.transpose():
#     print(*i)


# n = int(input())
# matrix = [['.' for _ in range(n)] for i in range(n)]
# for i in range(n):
#     matrix[i][i] = '*'
#     matrix[i][n-i-1] = '*'
# matrix[(n - 1)//2] = ['*' for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if j == (n - 1)//2:
#             matrix[i][j] = '*'
# for i in matrix:
#     print(*i)

# def foo(m):
#     a, b, c, d = [], [], len(m) - 1, 0
#     for i in range(len(m)):
#         a += m[i][:c]
#         b += m[i][d:]
#         c -= 1
#         d -= 1
#     r = set(a + b[len(m[0]):])
#     return 'YES' if len(r) == len(a) else 'NO'
# print(foo([[int(_) for _ in input().split()] for i in range(int(input()))]))

# sizes, counter, symmetry = int(input()), 0, True
# matrix = [input().split() for _ in range(sizes)]
# for i in range(sizes):
#     for j in range(sizes):
#         if i + j + 1 < sizes:
#             if matrix[i][j] == matrix[sizes - 1 - j][sizes - 1 - i]:
#                 counter += 1
#             else:
#                 print('NO')
#                 symmetry = False
#                 quit()
# if symmetry:
#     print('YES')

# n = int(input())
# matrix = [[int(_) for _ in input().split()] for i in range(n)]
# for i in range(n):
#     if sorted(matrix[i]) != list(range(1, n + 1)) or sorted([matrix[j][i] for j in range(n)]) != list(range(1, n + 1)):
#         print('NO')
#         break
# else:
#     print('YES')

x = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
y = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7, '0': 8}
matrix = [['.' for _ in range(8)] for i in range(8)]
for i in matrix:
    print(*i)

# abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2
