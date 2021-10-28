class Queue:
    """
    Очередь - структура данных, в которой первый помещённый элемент является первым извлекаемым.
    'Первым вошёл - первым вышел', FIFO (first-in-first-out)
    """

    def __init__(self):
        """Метод __init__ создаёт новую пустую очередь."""
        self.items = []
        self.queuestart = 0

    def isempty(self):
        """Метод isempty() проверяет очередь на пустоту."""
        return len(self.items) == 0

    def top(self):
        """Метод top() возвращает первый элемент очереди, но не удаляет его."""
        if self.items:
            return self.items[self.queuestart]
        return None

    def bottom(self):
        """Метод bottom() возвращает последний элемент очереди, но не удаляет его."""
        if self.items:
            return self.items[-1]
        return None

    def push(self, item):
        """Метод push() добавляет новый элемент в очередь."""
        return self.items.append(item)

    def pop(self):
        """Метод pop() удаляет первый элемент из очереди."""
        if self.items:
            result = self.items[self.queuestart]
            self.queuestart += 1  # "ленивое удаление" неиспользуемых элементов
            if self.queuestart > len(self.items) / 2:  # критерий реального удаления неиспользуемых элементов
                self.items[:self.queuestart] = []
                self.queuestart = 0
            return result
        return None

    def size(self):
        """Метод size() возвращает количество элементов в очереди."""
        return len(self.items) - self.queuestart

    def clear(self):
        """Метод clear() очищает вcю очередь."""
        if self.items:
            self.items[:] = []
            return
        return None
