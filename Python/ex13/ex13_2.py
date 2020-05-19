from sys import argv
script,first,third = argv
print('当前的路径是：',script)
print(first)
print(third)
age = int(input('你的年龄：'))
tall = int(input('你的身高：'))
print('所以你的年龄✖️身高等于',age * tall)