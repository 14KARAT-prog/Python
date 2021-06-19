a = [[1, 2, 3, 4], [1, 1, 2, 4], [1, 6, 7, 9]]
b = [[0, 5, 4, 3], [0, 3, 1, 5], [6, 7, 8, 3]]


class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        a = []
        for i in range(len(self.list)):
            for n in range(len(self.list[0])):
                a[i].append(self.list[i][n] + other.list[i][n])

        return '\n'.join(map(str, a))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
