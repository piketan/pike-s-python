from sys import argv

script,filename = argv

print(f"我们现在要改写这个{filename}文件")
print("filename,'w'的意思就是以读写的方式打开filename")
target = open(filename,'w')

print(f"我们现在要用target.truncate()清空{filename}的内容")
target.truncate()
print("输入你要加进去的内容")
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
print("完毕")