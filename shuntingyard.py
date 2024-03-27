from stack import Stack


def shunting_yard(Input: list) -> list:
    if Input == []:
        return ['']

    unclosed_parentheses = 0
    basic_operators = ('+', '-', '^', '*', '/')
    lower_predence = basic_operators[:2]
    higher_predence = basic_operators[3:]
    opstack = []  # Output.
    stack = []

    for cval in Input:

        if isinstance(cval,int) or isinstance(cval,float):
            opstack.append(cval)

        elif cval == '(':
            if ')' not in Input:
                return ['\0', 'UNCLOSED "("']
            stack.append(cval)
            unclosed_parentheses += 1

        elif cval == ')':
            if '(' not in stack:
                return ['\0', 'UNMATCHING ")"']

            while stack[-1] != '(':
                opstack.append(stack.pop(-1))
            del stack[-1]

            unclosed_parentheses -= 1

        elif cval in lower_predence:
            if len(stack) > 0 and '(' not in stack:
                for i in range(len(stack)):
                    opstack.append(stack.pop(-1))
            stack.append(cval)

        elif cval in higher_predence:
            if len(stack) > 0:
                if '(' not in stack or stack[-1] in lower_predence:
                    while stack[-1] in higher_predence or stack[-1] == '^':
                        opstack.append(stack.pop(-1))
            stack.append(cval)

        elif cval == '^':
            stack.append(cval)

    for i in range(len(stack)):
        opstack.append(stack.pop(-1))
    return opstack
