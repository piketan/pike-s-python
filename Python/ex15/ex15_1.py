
from sys import argv

path = "/pike-s-python/Python/ex15/"
txt = open(path+'ex15.txt')

print(f"这是你的文件{txt}")
print(txt.read())
print("再一次输入文件名")
file_again = input(">")

txt_again = open(path+file_again)

print(txt_again.read())