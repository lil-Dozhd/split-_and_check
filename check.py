def skobke(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0

test_expressions = [
    "",
    ")",
    "()",
    "{[()]}",
    "({[})",
    "((())",
    "()[]{}",
]

for expr in test_expressions:
    print(f"{expr}: {skobke(expr)}")