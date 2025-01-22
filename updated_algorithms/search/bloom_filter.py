"""
Bloom filter — это вероятностная структура данных, которая используется для проверки наличия элемента в наборе.
Она даёт возможность быстро определить, является ли элемент «возможно в наборе» или «точно не в наборе»,
но с некоторой вероятностью может возвращать ложноположительные результаты (false positives).
Bloom фильтры применяются там, где требуется экономия памяти и скорость доступа, а точность не критична.

Bloom-фильтры не допускают ложноотрицательных результатов (то есть они никогда не скажут, что элемент отсутствует,
если он был добавлен), но могут давать ложноположительные результаты — сообщать, что элемент в наборе,
хотя его там на самом деле нет.
"""

from bitarray import bitarray
import mmh3


class BloomFilter:

    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = 1

    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == 0:
                return False
        return True


bloom = BloomFilter(5000, 7)

bloom.add("apple")

print(bloom.check("apple"))  # Ожидаем True (возможно, элемент в наборе).
print(bloom.check("banana"))  # Ожидаем False (точно нет в наборе).
