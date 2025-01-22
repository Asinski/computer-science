class ChainSum6(int):
    def __call__(self, addition=0):
        return ChainSum6(self + addition)


print(1 + ChainSum6(5))
print(1 + ChainSum6(5)())
print(1 + ChainSum6(5)(10))
