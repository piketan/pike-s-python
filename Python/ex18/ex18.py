def print_two(*args):
    arg1 , agr2 = args
    print(f"arg1:{arg1},arg2:{agr2}")

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")


def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print('这里啥都没有')

print_two("zed","Shaw")
print_two_again("zed",'shaw')
print_one("Fiel")
print_none()