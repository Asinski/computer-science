from typing import List


class Stack:

    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None


class ListOfIndex:
    def __init__(self, value, index):
        self.value = value
        self.index = index


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures = [ListOfIndex(v, i) for i, v in enumerate(temperatures)]
        diff = []
        stack_days = Stack()
        for i in range(len(temperatures) - 1, -1, -1):
            while not stack_days.isempty() and temperatures[i].value >= stack_days.peek().value:
                stack_days.pop()
            if not stack_days.isempty():
                diff.append(stack_days.peek().index - i)
            if stack_days.isempty():
                diff.append(0)
            stack_days.push(temperatures[i])

        return diff
