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


def rezolvare(raw_exp):

#Returneaza solutia
    try:
        postfix_exp = _postfixare_(_tokenizare_expresie(raw_exp))
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

# Solutia va fi ultimul nr ramas in stiva
        solution = round(number_stack.pop(), 15)

#Remediaza eroarea de la round +/- 0  
        if solution == -0:
            solution += 0

        return solution
    except Exception:
        print("Eroare!")
        exit()




def _tokenizare_expresie(raw_exp):
    tokenized_exp = []
    next_num, next_alpha = '', ''

    for char in raw_exp:
        if _is_number(char) or char == '.':
            if len(next_alpha) > 0:
                tokenized_exp.append(next_alpha)
                next_alpha = ''
            next_num += char
        elif char.isalpha():
            if len(next_num) > 0:
                tokenized_exp.append(next_num)
                next_num = ''
            next_alpha += char
        elif char in operators or char == '(' or char == ')':
            if len(next_num) > 0:
                tokenized_exp.append(next_num)
                next_num = ''
            elif len(next_alpha) > 0:
                tokenized_exp.append(next_alpha)
                next_alpha = ''
            tokenized_exp.append(char)

    
    if len(next_num) > 0:
        tokenized_exp.append(next_num)
    if len(next_alpha) > 0:
        tokenized_exp.append(next_alpha)

    return tokenized_exp


def _postfixare_(infix_exp):
    postfix_exp, op_stack = [], []

    for token in infix_exp:
        if _is_number(token):
            postfix_exp.append(token)
        elif token in operators:
            while ((len(op_stack) > 0 and op_stack[-1] in operators) and
                    ((token != '^' and
                        operators[token][0] <= operators[op_stack[-1]][0]) or
                    (token == '^' and
                        operators[token][0] < operators[op_stack[-1]][0]))):
                postfix_exp.append(op_stack.pop())
            op_stack.append(token)
        elif token in functions:
            op_stack.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while len(op_stack) > 0 and op_stack[-1] != '(':
                postfix_exp.append(op_stack.pop())
            op_stack.pop()
            if len(op_stack) > 0 and op_stack[-1] in functions:
                postfix_exp.append(op_stack.pop())
    while len(op_stack) > 0:
        postfix_exp.append(op_stack.pop())

    return postfix_exp


def _is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    running = True

    while running:
        user_input = input('Calcul:')
        if user_input == 'exit':
            running = False
        else:
            print(rezolvare(user_input))
