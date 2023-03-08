def backspace_compare(s,t):
    if not s and not t: return True
    if not s or not t: return False
    stack = []
    stack2 = []

    for i in range(len(s)):
        if s[i] != "#":
            stack.append(s[i])
        else:
            if not stack: continue
            stack.pop()

    for i in range(len(t)):
        if t[i] != "#":
            stack2.append(t[i])
        else:
            if not stack2: continue
            stack2.pop()
    return stack == stack2
res = backspace_compare("ab#c","ad#c")
print(res)
