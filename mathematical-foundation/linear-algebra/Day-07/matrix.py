# ==========================================
# WEEK 5 PROJECT
# Matrix Class in Pure Python (No NumPy)
# ==========================================


class Matrix:

    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def display(self):
        for row in self.data:
            print(row)

   
    def add(self, other):

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")

        result = []

        for i in range(self.rows):

            row = []

            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])

            result.append(row)

        return Matrix(result)


    def subtract(self, other):

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")

        result = []

        for i in range(self.rows):

            row = []

            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])

            result.append(row)

        return Matrix(result)

 
    def multiply(self, other):

        if self.cols != other.rows:
            raise ValueError(
                "Number of columns of first matrix must equal rows of second matrix."
            )

        result = []

        for i in range(self.rows):

            row = []

            for j in range(other.cols):

                value = 0

                for k in range(self.cols):

                    value += self.data[i][k] * other.data[k][j]

                row.append(value)

            result.append(row)

        return Matrix(result)

  
    def transpose(self):

        result = []

        for j in range(self.cols):

            row = []

            for i in range(self.rows):
                row.append(self.data[i][j])

            result.append(row)

        return Matrix(result)




A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])

B = Matrix([
    [7, 8, 9],
    [10, 11, 12]
])

C = Matrix([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("=" * 50)
print("Matrix A")
print("=" * 50)
A.display()

print("\n")

print("=" * 50)
print("Matrix B")
print("=" * 50)
B.display()

print("\n")

print("=" * 50)
print("Addition")
print("=" * 50)
A.add(B).display()

print("\n")

print("=" * 50)
print("Subtraction")
print("=" * 50)
A.subtract(B).display()

print("\n")

print("=" * 50)
print("Transpose of Matrix A")
print("=" * 50)
A.transpose().display()

print("\n")

print("=" * 50)
print("Matrix C")
print("=" * 50)
C.display()

print("\n")

print("=" * 50)
print("Matrix Multiplication (A × C)")
print("=" * 50)
A.multiply(C).display()
