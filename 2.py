class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


def is_balanced(s):
    stack = Stack()
    brackets = {"(": ")", "{": "}", "[": "]"}

    for bracket in s:
        if bracket in brackets:
            stack.push(bracket)
        elif stack.is_empty() or brackets[stack.pop()] != bracket:
            return "Несбалансированно"
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


# Проверка
print(is_balanced("(((([{}]))))"))  # Сбалансированно
print(is_balanced("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(is_balanced("{{[()]}}"))  # Сбалансированно
print(is_balanced("}{"))  # Несбалансированно
print(is_balanced("{{[(])]}}"))  # Несбалансированно
print(is_balanced("[[{())}]"))  # Несбалансированно
