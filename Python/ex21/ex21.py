def add(a,b):
    print(f"相加{a}+{b}")
    return a+b

def subtract(a,b):
    print(f"相减{a}-{b}")
    return a-b

def multiply(a,b):
    print(f"相乘{a}*{b}")
    return a*b

def divide(a,b):
    print(f"相除{a}/{b}")
    return a/b

print("函数做一些简单的计算")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"年龄：{age},身高：{height},体重：{weight},iq：{iq}")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("变成",what)

