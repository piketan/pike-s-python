#python-读写文件
    close:在python中的作用大致是保存并关闭
    read:读取文件的内容，可以把文件里的内容赋予一个变量
    readline:只读取文本中的一行
    truncate:清空文件内容    open(filename,'w+')如果写法用了w的话就不需要用truncate清空文件内容
    write(''):write是改写状态括号内是需要改写的内容例：write('stuff') 将stuff写入文件
    seek(0):将读写位置移动到文件开头