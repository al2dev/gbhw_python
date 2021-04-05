

class Matrix:
    def __init__(self, m):
        self.m = m

    def __str__(self):
        return '\n'.join([' '.join(map(str, s)) for s in self.m])


class Clothes:
    cloth = 0

    def __init__(self, q):
        self.copy_cloth = q
        Clothes.cloth += self.copy_cloth

    def __del__(self):
        Clothes.cloth -= self.copy_cloth


class Coat(Clothes):
    def __init__(self, v):
        self.__q = v / 6.5 + 0.5
        Clothes.__init__(self, self.__q)


class Jacket(Clothes):
    def __init__(self, h):
        self.__q = 2 * h + 0.3
        Clothes.__init__(self, self.__q)


class Biocell:
    def __init__(self, cell):
        self.cell = cell

    def make_order(self, count):
        return '\n'.join([''.join([gen for gen in ('*' for n in range(count))]) for s in range(self.cell // count)]) + \
              '\n' + ''.join([gen for gen in ('*' for n in range(self.cell % count))])

    def __add__(self, other):
        return Biocell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell > other.cell:
            self.cell = self.cell - other.cell
            del other
        else:
            other.cell = other.cell - self.cell
            del self
        return self if self else other

    def __mul__(self, other):
        return Biocell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Biocell(self.cell // other.cell)

    def __truediv__(self, other):
        return Biocell(self.cell // other.cell)


if __name__ == '__main__':
    # 1 task
    print('\n')
    print('Task 1')
    m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    m2 = Matrix([[1, 2], [3, 4], [5, 6]])
    print(m1)
    print(m2)

    # 2 task
    print('\n')
    print('Task 2')
    c_1 = Coat(5)
    print(Clothes.cloth)
    c_2 = Coat(5)
    print(Clothes.cloth)
    j_3 = Jacket(5)
    print(Clothes.cloth)
    del c_1
    print(Clothes.cloth)
    del c_2
    print(Clothes.cloth)
    del j_3
    print(Clothes.cloth)

    # 3 task

