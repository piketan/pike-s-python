from sys import argv
from os.path import exists

scrpit,from_file,to_file = argv

print(f"将{from_file}的内容复制到{to_file}")

in_file = open(from_file)
indata = in_file.read()
print(f"{from_file}文件的有{len(indata)}bytes")

print(f"检查{to_file}是否存在{exists(to_file)}")
print("现在开始复制")

out_file = open(to_file,'w')
out_file.write(indata)

print('复制完成')

out_file.close()
in_file.close()


