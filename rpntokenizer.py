from queue import Queue



def tokenize_rpn(Input: list) -> list:
    operators = ['+', '-', '(', ')', '*', '/', '^']
    output = []


    while len(Input):
        current_token = Input.pop(0)

        if current_token.isdigit():
            while len(Input) and Input[0].isdigit():
                current_token += Input.pop(0)
            if len(Input) and Input[0] == '.':
                current_token += Input.pop(0)
                while len(Input) and Input[0].isdigit():
                    current_token += Input.pop(0)

            current_token = float(current_token) if '.' in current_token \
                                                 else int(current_token)

        output.append(current_token)

    return output
