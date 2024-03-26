def calculation(rpn):
    tempstack = []  # Temporarily stores the rpn as it is read.

    for cval in rpn:

        if isinstance(cval,int) or isinstance(cval,float):
            tempstack.append(cval)

        elif isinstance(cval,str):
            try:
                sval = tempstack.pop(-1)  # Second value.
                fval = tempstack.pop(-1)  # First value.
            except IndexError:
                return ''

            if cval == '+':
                tempstack.append(fval + sval)
            elif cval == '-':
                tempstack.append(fval - sval)
            elif cval == '*':
                tempstack.append(fval * sval)
            elif cval == '/':
                tempstack.append(fval / sval)
            elif cval == '^':
                tempstack.append(fval ** sval)

    return round(tempstack[0],3)
