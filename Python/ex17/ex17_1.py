from sys import argv
from os.path import exists
scrpit,from_file,to_file = argv
indata = open(from_file).read()
print(f"{from_file}有{len(indata)}bytes字节")
print(f"检查{to_file}是否存在 检查结果：{exists(to_file)}")
open(to_file,'w').write(indata)
print('复制完成')



