class DoublyLinkedList:
    """
    LinkedList, или связанный список – массив, где каждый элемент является отдельным объектом
    и состоит из двух элементов – данных и ссылки на следующий узел.

    Двунаправленный: две ссылки, связанные с каждым узлом, – c предыдущим и последующим узлами.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    class Node:
        def __init__(self, item, prev_node=None, next_node=None):
            self.item = item
            self.prev_node = prev_node
            self.next_node = next_node

    def isempty(self):
        """Метод isempty() проверяет двусвязный список на пустоту."""
        if self.length:
            return False
        return True

    def contains(self, item):
        """Метод contains() проверяет наличие элемента в двусвязном списке."""
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
                self.lappend(new_item)
            else:
                index_node = 0
                node = self.head
                previous_node = self.head
                while index_node < index_item:
                    previous_node = node
                    node = node.next_node
                    index_node += 1
                new_node = self.Node(new_item, prev_node=node.prev_node, next_node=node)
                previous_node.next_node = new_node
                self.length += 1

    def lappend(self, new_item):
        """Метод lappend() позволяет вставить новый элемент в начало двусвязного списка."""
        if not self.isempty():
            self.head.prev_node = self.Node(new_item, next_node=self.head)
            self.head = self.head.prev_node
            self.length += 1
        else:
            self.append(new_item)

    def append(self, new_item):
        """Метод append() добавляет новый элемент в конец двусвязного списка за O(1)."""
        new_node = self.Node(new_item)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            node = self.tail
            new_node.prev_node = self.tail
            node.next_node = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, item):
        """Метод remove() удаляет первое вхождение заданного элемента."""
        if not self.isempty():
            if self.length == 1:
                self.pop()
            else:
                node = self.head
                if node.item == item:
                    self.head = node.next_node
                    self.head.prev_node = None
                else:
                    previous_node = self.head
                    while node:
                        if node.item == item:
                            break
                        previous_node = node
                        node = node.next_node
                    if node is None:
                        return f'Данного элемента в списке нет.'
                    node.next_node.prev_node = node.prev_node
                    previous_node.next_node = node.next_node
                self.length -= 1
        else:
            print(None)

    def lpop(self):
        """Метод lpop() позволяет удалить первый элемент из двусвязного списка."""
        if not self.isempty():
            popitem = self.head.item
            if self.length == 1:
                self.pop()
            else:
                self.head = self.head.next_node
                self.head.prev_node = None
                self.length -= 1
                return popitem
        else:
            print(None)

    def pop(self):
        """Метод pop() удаляет последний элемент двусвязного списка за O(1)."""
        if not self.isempty():
            popitem = self.tail.item
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev_node
                self.tail.next_mode = None
            self.length -= 1
            return popitem
        else:
            print(None)

    def print(self, reversed=False):
        """Метод print() отображает весь двусвязный список."""
        if not self.isempty():
            if not reversed:
                node = self.head
                while node.next_node:
                    print(node.item, end=" ")
                    node = node.next_node
            else:
                node = self.tail
                while node.prev_node:
                    print(node.item, end=" ")
                    node = node.prev_node
            print(node.item)
        else:
            print(None)

    def clear(self):
        """Метод сlear() очищает весь двусвязный список."""
        self.head = self.tail = None
        self.length = 0
