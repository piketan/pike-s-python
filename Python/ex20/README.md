#python 解释这一章每一栏的作用
    from sys import argv
    #引入sys这个库使用argv这个模块
    script,input_file =argv
    #script是argv自带的变量 它的作用就是显示当前文件路径
    def print_all(f):
    #定义一个函数 print_all f是这个函数里的变量
    print(f.read())
    #将f这个函数以读写状态打印出来
    def rewind(f):
    #定义一个函数 rewind f是这个函数里的变量
    f.seek(0)
    #移动到文件的开头
    def print_a_line(line_count,f):
    print(line_count,f.readline())
    #定义一个函数 line_count f是这个函数里的变量
    current_file = open(input_file)
    #打开input_file这个变量的文件
    print("首先我们将打印这个文件 file:\n")

    print_all(current_file)
    #将current_file赋予函数print_all里的变量
    print("现在倒放下这个文件")
    rewind(current_file)
    #将current_file赋予函数current_file里的变量
    print("现在打印这个文件的第三行:")
    current_line = 1
    print_a_line(current_line,current_file)

    current_line = current_line + 1
    print_a_line(current_line,current_file)

    current_line = current_line + 1
    print_a_line(current_line,current_file)