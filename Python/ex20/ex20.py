from sys import argv

script,input_file =argv
print(script)
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file = open(input_file)

print("首先我们将打印这个文件 file:\n")

print_all(current_file)

print("现在倒放下这个文件")

rewind(current_file)

print("现在打印这个文件的第三行:")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)