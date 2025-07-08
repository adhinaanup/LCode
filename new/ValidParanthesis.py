def isValid(exp):
    stack=[]
    mapping={')':'(',']':'[','}':'{'}
    for ch in exp:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1]!=mapping[ch]:
                return False
            else:
                stack.pop()
    return not stack
exp=input("Enter the expression : ")
if(isValid(exp)):
    print("Valid parenthesis")
else:
    print("Invalid parathesis")
