class SinglyLinkedList:
    """
    LinkedList, или связанный список – массив, где каждый элемент является отдельным объектом
    и состоит из двух элементов – данных и ссылки на следующий узел.

    Однонаправленный: каждый узел хранит ссылку на следующий узел в списке,
    а последний узел имеет следующую ссылку как NULL.
    """

    def __init__(self):
        self.head = None
        self.length = 0

    class Node:
        def __init__(self, item, next_node=None):
            self.item = item
            self.next_node = next_node

    def isempty(self):
        """Метод isempty() проверяет односвязный список на пустоту."""
        if self.length:
            return False
        return True

    def contains(self, item):
        """Метод contains() проверяет наличие элемента в односвязном списке."""
        node = self.head
        while node:
            if item == node.item:
                return True
            node = node.next_node
        return False

    def getitem(self, index_item):
        """Метод getitem() позволяет обратиться к элементу по заданному индексу."""
        if not self.isempty():
            if index_item < 0:
                return f'Отрицательные индексы не поддерживаются.'
            if index_item <= self.length - 1:
                index_node = 0
                node = self.head
                while index_node <= index_item:
                    if index_node == index_item:
                        return node.item
                    index_node += 1
                    node = node.next_node
            return f'Вы вышли за границы списка: максимальный индекс - {self.length - 1}.'
        else:
            print(None)

    def insert(self, new_item, index_item):
        """Метод insert() вставляет новый элемент по заданному индексу."""
        if self.isempty():
            self.append(new_item)
        else:
            if index_item == 0:
                self.head = self.Node(new_item, next_node=self.head)
            else:
                index_node = 0
                node = self.head
                prev_node = self.head
                while index_node < index_item:
                    prev_node = node
                    node = node.next_node
                    index_node += 1
                new_node = self.Node(new_item, next_node=node)
                prev_node.next_node = new_node
            self.length += 1

    def append(self, new_item):
        """Метод append() добавляет новый элемент в конец односвязного списка за O(self.length)."""
        new_node = self.Node(new_item)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = new_node
        self.length += 1

    def remove(self, item):
        """Метод remove() удаляет первое вхождение заданного элемента."""
        if not self.isempty():
            node = self.head
            if node.item == item:
                self.head = node.next_node
            else:
                prev_node = self.head
                while node:
                    if node.item == item:
                        break
                    prev_node = node
                    node = node.next_node
                if node is None:
                    return f'Данного элемента в списке нет.'
                prev_node.next_node = node.next_node
            self.length -= 1
        else:
            print(None)

    def pop(self):
        """Метод pop() удаляет последний элемент односвязного списка за O(self.length)."""
        if not self.isempty():
            if self.length == 1:
                popitem = self.head.item
                self.head = None
                self.length -= 1
                return popitem
            else:
                prev_node = self.head
                node = self.head
                while True:
                    if node.next_node is None:
                        popitem = prev_node.next_node
                        prev_node.next_node = node.next_node
                        self.length -= 1
                        return popitem.item
                    prev_node = node
                    node = node.next_node
        else:
            print(None)

    def print(self):
        """Метод print() отображает весь односвязный список."""
        if not self.isempty():
            node = self.head
            while node.next_node:
                print(node.item, end=" ")
                node = node.next_node
            print(node.item)
        else:
            print(None)

    def clear(self):
        """Метод сlear() очищает весь односвязный список."""
        self.head = None
        self.length = 0
