# s=lambda a,b:a*b
# print(s(2,4))


# def fun(a):
#     return lambda b:a+b
# x=fun(2)
# print(x(3))


##functional programing


def add(a,b):
    return a+b

def sqr(x):
    return x**2
z=sqr(add(5,3))
print(z)