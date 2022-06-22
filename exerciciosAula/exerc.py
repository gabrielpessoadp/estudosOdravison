def f2(a):
    return a*a

def f1(a,b):
    if a > b:
        return 0
    else:
        return f2(a) + f1(a + 1, b)

def funcao(x):
    if x <= 1:
        return x
    else:
        return funcao(x - 1) + funcao(x - 2)
