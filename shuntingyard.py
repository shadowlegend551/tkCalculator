from stack import Stack
from queue import Queue


def shunting_yard(Input: Queue) -> list:
    if Input.isEmpty():
        return Stack([''])

    unclosed_parentheses = 0
    basic_operators = ('+', '-', '^', '*', '/')
    lower_predence = basic_operators[:2]
    higher_predence = basic_operators[3:]
    opstack = Stack()
    stack = Stack()

    for cval in Input.queue:

        if isinstance(cval,int) or isinstance(cval,float):
            opstack.push(cval)

        elif cval == '(':
            if ')' not in Input.queue:
                return ['\0', 'UNCLOSED "("']
            stack.push(cval)
            unclosed_parentheses += 1

        elif cval == ')':
            if '(' not in stack.stack:
                return ['\0', 'UNMATCHING ")"']

            while stack.check() != '(':
                opstack.push(stack.pop())
            stack.pop()

            unclosed_parentheses -= 1

        elif cval in lower_predence:
            if not stack.isEmpty() and '(' not in stack.stack:
                for i in range(stack.length()):
                    opstack.push(stack.pop())
            stack.push(cval)

        elif cval in higher_predence:
            if not stack.isEmpty():
                if '(' not in stack.stack or stack.check() in lower_predence:
                    while stack.check() in higher_predence or stack.check() == '^':
                        opstack.append(stack.pop())
            stack.push(cval)

        elif cval == '^':
            stack.push(cval)

    for i in range(stack.length()):
        opstack.push(stack.pop())
    return opstack.stack

