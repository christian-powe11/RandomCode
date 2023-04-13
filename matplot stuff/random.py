s = "()[]([])"


def func(s):
    a,b,d = [], [],[]
    for c in s:
        if c == '(':
            a.append('(')
        elif c == ')':
            a.pop()
        elif c == '[':
            b.append('[')
        elif c == ']':
            b.pop()
        elif c == '{':
            d.append('{')
        elif c == '}':
            d.pop()
        else:
            continue
    if (not a and not b and not d):
        return True
    else:
        return False
    
print(func(s))


def fact(n):
    if n == 1: return 1
    else: return n*fact(n-1)

print(fact(5))
