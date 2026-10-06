def evaluate(expression):
    values = []
    operators = []

    for ch in expression:
        if ch.isdigit():
            values.append(int(ch))

        elif ch in "+-*/":
            while operators:
                b = values.pop()
                a = values.pop()
                op = operators.pop()

                if op == '+':
                    values.append(a + b)
                elif op == '-':
                    values.append(a - b)
                elif op == '*':
                    values.append(a * b)
                elif op == '/':
                    values.append(a / b)

            operators.append(ch)

    while operators:
        b = values.pop()
        a = values.pop()
        op = operators.pop()

        if op == '+':
            values.append(a + b)
        elif op == '-':
            values.append(a - b)
        elif op == '*':
            values.append(a * b)
        elif op == '/':
            values.append(a / b)

    return values[-1]

expression = "2+3*4"
print("Expression:", expression)
print("Result:", evaluate(expression))