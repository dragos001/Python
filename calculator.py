import math


operators = {
    '+': (1, lambda a, b: a + b),
    '-': (1, lambda a, b: a - b),
    '*': (2, lambda a, b: a * b),
    '/': (2, lambda a, b: a / b),
    '%': (2, lambda a, b: a % b),
    '^': (3, lambda a, b: a ** b)
}


functions = {
    'rad': (1, lambda a: math.sqrt(a)),
    'sin': (1, lambda a: math.sin(a)),
    'asin': (1, lambda a: math.asin(a)),
    'cos': (1, lambda a: math.cos(a)),
    'acos': (1, lambda a: math.acos(a)),
    'tan': (1, lambda a: math.tan(a)),
    'atan': (1, lambda a: math.atan(a)),
    'log': (1, lambda a: math.log10(a)),
    'ln': (1, lambda a: math.log(a))
}


def solve(raw_exp):
    """Return the solution of the provided raw expression"""
    postfix_exp = _to_postfix(_tokenize_expression(raw_exp))
    number_stack = []

    for token in postfix_exp:
        if _is_number(token):
            number_stack.append(float(token))
        elif token in operators:
            temp = number_stack.pop()
            number_stack.append(operators[token][1](number_stack.pop(), temp))
        elif token in functions:
            if functions[token][0] == 1:
                number_stack.append(functions[token][1](number_stack.pop()))


    solution = round(number_stack.pop(), 15)

    
    if solution == -0:
        solution += 0

    return solution

def _is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
