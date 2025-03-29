from typing import Union


class CustomList(list):
    """CustomList"""

    @staticmethod
    def add_func(x: Union[int, float], y: Union[int, float]):
        """Сумма двух чисел"""
        return x + y

    @staticmethod
    def sub_func(x: Union[int, float], y: Union[int, float]):
        """Разность двух чисел"""
        return x - y

    def __add__(self, other):
        return CustomList(map(self.add_func, self, other))

    def __radd__(self, other):
        return CustomList(map(self.add_func, self, other))

    def __sub__(self, other):
        return CustomList(map(self.sub_func, self, other))

    def __rsub__(self, other):
        return CustomList(map(self.sub_func, other, self))

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f"{self[:]}, {sum(self[:])}"
