txt = input("请输入你要打开的文件名：")
txts = open(txt)
print("这是你的文件名{}".format(txt))
print(txts.read())