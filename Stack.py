class Stack:

    def __init__(self, stack: str = ''):
        self.stack = list(stack)

    def is_empty(self):
        if len(self.stack) >= 1:
            return True
        else:
            return False

    def m_push(self, object_1):
        self.stack.append(object_1)

    def m_pop(self):
        return self.stack.pop()

    def m_peek(self):
        result = self.stack[-1]
        return result

    def size(self):
        result = len(self.stack)
        return result
