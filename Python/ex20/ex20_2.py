#from sys import argv
# 引入sys这个库使用argv这个模块
#script, input_file = argv
# script是argv自带的变量 它的作用就是显示当前文件路径
def print_all(f):
    print(f.read())
# 定义一个函数 print_all f是这个函数里的变量
# 将f这个函数以读写状态打印出来
def rewind(f):
    f.seek(0)
# 定义一个函数 rewind f是这个函数里的变量
# 移动这个f这边变量的第一行
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open('ex20.txt','rb')

print("首先我们将打印这个文件 file:\n")

print_all(current_file)

print("现在倒放下这个文件")

rewind(current_file)

print("现在打印这个文件的第三行:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)