class Stack:
    def __init__(self):
        self.stack = []

    # проверка стека на пустоту
    def is_empty(self):
        return len(self.stack) == 0

    # добавляет новый элемент на вершину стека
    def push(self, item):
        self.stack.append(item)

    # удаляет верхний элемент стека
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    # возвращает верхний элемент стека, но не удаляет его
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    # возвращает количество элементов в стеке
    def size(self):
        return len(self.stack)
