class ChainSum5:
    def __init__(self, number):
        self._number = number

    def __call__(self, value=0):
        return ChainSum5(self._number + value)

    def __str__(self):
        return str(self._number)


print(ChainSum5(5))
print(ChainSum5(5)())
print(ChainSum5(5)(2))
print(ChainSum5(5)(100)(-10))
