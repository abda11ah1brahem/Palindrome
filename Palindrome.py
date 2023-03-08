def isPalindrome(str):
    stack=[]
    p=False
    for s in str:
        stack.append(s)
    for s in str:
        if s==stack.pop():
            p=True
        else:
            p=False
    return p
print(isPalindrome("smadams"))