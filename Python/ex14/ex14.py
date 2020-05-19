from sys import argv
script,user_name = argv
prompt = '>'

print(f"嘿 {user_name},我是{script}里的脚本")
print("我想问你几个小问题")
print(f"你喜欢这个脚本吗 {user_name}")
likes = input(prompt)

print("你现在住在哪里呢")
lives = input(prompt)

print("你有一台怎么样的电脑呢")
computer = input(prompt)
print(f'''
\f好的，所以说你{likes}这个脚本
\f你现在住在{lives}
\f你有一台{computer}的电脑
''')

print(f"好的，所以说你{likes}这个脚本\t\n你现在住在{lives}\t\n你有一台{computer}的电脑")