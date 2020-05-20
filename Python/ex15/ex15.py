from sys import argv

script,filename = argv

txt = open(filename)

print(f"这是你的文件{filename}")
print(txt.read())

print("再一次输入文件名")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
