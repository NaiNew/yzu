def calc(x=1, y=2, z=None):
    if z == None:
        return x + y
    return (x + y) * z
print(calc())
print(calc(10))  # x=10
print(calc(y=10))  # y=10
print(calc(10, 20, 2))
