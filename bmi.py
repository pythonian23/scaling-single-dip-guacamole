class Person:
    def __init__(self, **kwargs):
        if "weight" in kwargs:
            self._w = kwargs["weight"]
        else:
            self._w = -1
        if "height" in kwargs:
            self._h = kwargs["height"]
        else:
            self._h = -1

    @property
    def weight(self):
        if self._w < 0:
            raise RuntimeError("Weight not set")
        return self._w

    @weight.setter
    def weight(self, v):
        if v <= 0:
            raise ValueError("Weight must be larger than 0")
        self._w = v

    @property
    def height(self):
        if self._h < 0:
            raise RuntimeError("Height not set")
        return self._h

    @height.setter
    def height(self, v):
        if v <= 0:
            raise ValueError("Height must be larger than 0")
        self._h = v

    def set_from_input(self):
        self.weight = float(input("Kg: "))
        self.height = float(input("M : "))

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


p = Person()
p.set_from_input()
print(round(p.bmi, 1))
