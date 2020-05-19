print("你今年多大了",end='')
age = input()
print("你现在多高",end="")
tall = input()
print('你现在体重多少',end="")
weight = input()

print(f"所以你的年龄是{age},身高是{tall},体重是{weight}")

print("用input写的另一段")
print("这是一个猜数字游戏")
number = input("请输入初始数字：")
numbers = input("请输入你猜的数字：")
if number < numbers:
    print("大了")
elif number > numbers:
    print("小了")

elif number == numbers:
    print("恭喜您猜对了!!")



