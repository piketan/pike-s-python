f = open('ex20.txt', 'rb')
# 判断文件指针的位置
print(f.tell())
# 读取一个字节，文件指针自动后移1个数据
print(f.read(2))
print(f.tell())
# 将文件指针从文件开头，向后移动到 5 个字符的位置
f.seek(5)
print(f.tell())
print(f.read(1))
# 将文件指针从当前位置，向后移动到 5 个字符的位置
f.seek(5, 1)
print(f.tell())
print(f.read(1))
# 将文件指针从文件结尾，向前移动到距离 10 个字符的位置
f.seek(10, 1)
print(f.tell())
print(f.read(2))