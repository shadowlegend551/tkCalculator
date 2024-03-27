from queue import Queue



def tokenize_rpn(Input: list) -> Queue:
    operators = ['+', '-', '(', ')', '*', '/', '^']
    output = Queue()
    Input = Queue(Input)


    while not Input.isEmpty():
        current_token = Input.pop()

        if current_token.isdigit():
            while not Input.isEmpty() and Input.check().isdigit():
                current_token += Input.pop()
            if not Input.isEmpty() and Input.check() == '.':
                current_token += Input.pop()
                while not Input.isEmpty() and Input.check().isdigit():
                    current_token += Input.pop()

            current_token = float(current_token) if '.' in current_token \
                                                 else int(current_token)

        output.push(current_token)

    return output
