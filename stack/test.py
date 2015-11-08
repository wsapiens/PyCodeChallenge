str_data = '(1|0)^(1&0)'


def boolean_calculator(op, first, second):
    if op == '^':
        return int(first) ^ int(second)
    elif op == '|':
        return int(first) | int(second)
    elif op == '&':
        return int(first) & int(second)
    else:
        raise Exception('not an boolean operator')


def evaluate_boolean_expression(data):
    stack = []
    for ch in data:
        if ch == ')':
            while len(stack) > 1:
                second = stack.pop()
                op = stack.pop()
                if op == '(':
                    stack.append(second)
                    break
                first = stack.pop()
                stack.append(boolean_calculator(op, first, second))
        else:
            stack.append(ch)
    while len(stack) > 1:
        second = stack.pop()
        op = stack.pop()
        first = stack.pop()
        stack.append(boolean_calculator(op, first, second))
    print(stack[0])


if __name__ == '__main__':
    evaluate_boolean_expression(str_data)