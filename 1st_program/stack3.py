def evaluate(expression):
    stack = []

    for ch in expression:
        if ch.isdigit():
            stack.append(int(ch))

        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)

    return stack.pop()

expression = "23+5*"
print("Expression:", expression)
print("Result:", evaluate(expression))