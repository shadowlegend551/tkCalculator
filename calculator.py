def calculation(rpn: list) -> list:
    if rpn == ['']:
        return rpn

    tempstack = []  # Temporarily stores the rpn as it is read.

    for cval in rpn:

        if isinstance(cval,int) or isinstance(cval,float):
            tempstack.append(cval)

        elif isinstance(cval,str):
            if len(tempstack) >= 2:
                second_value = tempstack.pop(-1)  # Second value.
                first_operator = tempstack.pop(-1)  # First value.
            else:
                return ['\0', f'LONELY "{cval}"']

            if cval == '+':
                tempstack.append(first_operator + second_value)
            elif cval == '-':
                tempstack.append(first_operator - second_value)
            elif cval == '*':
                tempstack.append(first_operator * second_value)
            elif cval == '/':
                if second_value == 0: return ['\0', 'ZERO DIVISION']
                tempstack.append(first_operator / second_value)
            elif cval == '^':
                tempstack.append(first_operator ** second_value)

    return [str(round(tempstack[0],3))]
