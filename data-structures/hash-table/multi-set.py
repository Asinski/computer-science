class MultiSet:
    """
    Мультисет, или хэш-таблица - структура данных,
    содержащая уникальные элементы с адресацией, задаваемой хеш-функцией.
    """

    def __init__(self, size):
        self.size = size
        self.multiset = [[] for _ in range(size)]

    def add(self, item):
        """Метод add() добавляет новый элемент в мультисет"""
        if not self.find(item):
            self.multiset[item % self.size].append(item)

    def find(self, item):
        """Метод find() ищет переданный элемент в мультисете"""
        for now in self.multiset[item % self.size]:
            if now == item:
                return True
        return False

    def delete(self, item):
        """Метод delete() удаляет переданный элемент из мультисета."""
        itemlist = self.multiset[item % self.size]
        for i in range(len(itemlist)):
            if itemlist[i] == item:
                itemlist[i] = itemlist[-1]
                itemlist.pop()
                return
        return None

    def clear(self):
        """Метод clear() очищает весь мультисет."""
        if self.multiset:
            self.multiset = [[] for _ in range(self.size)]
            return
        return None
