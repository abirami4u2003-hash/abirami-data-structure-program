def evaluate_prefix(expression):
    stack = []

    tokens = expression.split()

    for token in reversed(tokens):

        if token.isdigit():
            stack.append(int(token))

        else:
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(a + b)

            elif token == '-':
                stack.append(a - b)

            elif token == '*':
                stack.append(a * b)

            elif token == '/':
                stack.append(a / b)

    return stack.pop()


expression = "- * 5 4 + 8 2"

print("Prefix Expression:", expression)
print("Result:", evaluate_prefix(expression))
