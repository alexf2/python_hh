class Adder:
    def __init__(self, value=0):
        self.value = value

    def __call__(self, value=None):
        if value is None:
            return self.value

        self.value += value

        return self


a = Adder()
print(a(1)(2)())

print(Adder()())

print(Adder(2)(5)(1)(10)())
