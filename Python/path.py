import os
for x in range(255,256):
 path = f'/pike-s-python/Python/ex{x}/'
 #os.mkdir(path)
 paths = open(path+'README'+'.md','w')
 #paths = open(path+f'ex{x}'+'.py','w')
 paths.close()
