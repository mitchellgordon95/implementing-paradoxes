from abc import ABC, abstractmethod


class Number(ABC):

    # Numbers should be comparable
    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other

    # Numbers should implement basic arithmetic
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def invert(self):
        pass

    @abstractmethod
    def __neg__(self):
        pass

    @abstractmethod
    def __abs__(self):
        pass

    def __sub__(self, other):
        return self + (-other)

    def __div__(self, other):
        return self * other.invert()

