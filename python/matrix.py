class Matrix:
     
    def __init__(self, date):
        self.date = date
    def __add__(self, other):
        a_row = len(self.date)
        a_col = len(self.date[0])

        b_row = len(other.date)
        b_col = len(other.date[0])



        if a_row != b_row and a_col != b_col:
            return "形状不同，不能相加"

            for row in range(a_row):
                for col in range(a_col):
                    self.date[row][col] += other.date[row][col]
                return self


 def __str__(self):
                    return str(self.date)


if __name__ == '__main__':
                    a = Matrix([[1,2],[3,4]])
                    b = Matrix([[5,6],[7,8]])
                    print(a + b)


#这个代码要好好的看一看





