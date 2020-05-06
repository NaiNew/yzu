def add(x):
    return x + 1

def sub(x):
    return x - 1

x = 10
x = add(x)
print(x)
x = sub(x)
print(x)

def operate(func, x):
    return func(x)

x = 10
x = operate(sub, x)
print(x)
