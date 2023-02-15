from Stack import Stack


def result(object_1):
    s = ['()', '{}', '[]']
    obj = Stack()
    for i in object_1:
        if i in '([{':
            obj.m_push(i)
        else:
            if obj.is_empty() is True and obj.m_peek() + i in s:
                obj.m_pop()
            else:
                return "Несбалансированно"

    if obj.size() == 0:
        return "Сбалансированно"
    else:
        return "Несбалансированно"
