def is_balanced(s):
    stack = []
    pairs = {"{": "}", "[": "]", "(": ")"}
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if len(stack) == 0 or pairs[stack.pop()] != char:
                return False
    if len(stack) > 0:
        return False
    return True


def main():
    string = "{[]{()}}}"
    print(is_balanced(string))

main()
