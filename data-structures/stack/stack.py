class Stack:
    """
    Стек - структура данных, в которой последний помещённый элемент является первым извлекаемым.
    'Последним вошёл - первым вышел', LIFO (last-in-first-out)
    """

    def __init__(self):
        """Метод __init__ создаёт новый пустой стек."""
        self.items = []

    def isempty(self):
        """Метод isempty() проверяет стек на пустоту."""
        return len(self.items) == 0

    def push(self, item):
        """Метод push() добавляет новый элемент на вершину стека."""
        return self.items.append(item)

    def pop(self):
        """Метод pop() удаляет верхний элемент из стека."""
        if self.items:
            return self.items.pop()
        return None

    def peek(self, index=-1):
        """Метод peek() возвращает верхний элемент стека, но не удаляет его."""
        if self.items:
            return self.items[index]
        return None

    def size(self):
        """Метод size() возвращает количество элементов в стеке."""
        return len(self.items)

    def clear(self):
        """Метод clear() очищает весь стек."""
        if self.items:
            self.items[:] = []
            return
        return None
