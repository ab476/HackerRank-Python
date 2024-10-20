if __name__ == '__main__':
    string = input()
    alphaNum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for s in string:
        if(s.isalnum()): alphaNum = True
        if(s.isalpha()): alpha = True
        if(s.isdigit()): digit = True
        if(s.islower()): lower = True
        if(s.isupper()): upper = True
    print(alphaNum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)