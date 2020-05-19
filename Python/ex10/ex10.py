tabby_cat = "\t\\t的作用就是自动在该字符串前打出四个空格"
persian_cat = "\\n的作用就是\n换行"
backslash_cat = "如果需要在字符串中\\n这样的写法就需要在\\n前再加一个\\"
chang_cat = "\n"

fat_cat = """
可以用一对三个双引号换行
\t换行1
\t换行2
\v换行
"""

fat_cat = '''
可以用一对三个双引号换行
\t换行1
\t换行2
\v换行
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(f"格式化字符和{chang_cat}转义的组合使用")
print(fat_cat)