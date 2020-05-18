name = 'Zed A. Shaw'
#变量的值如果加了单引号或者双引号的话就会变成字符串
age = 35
height = 74
weight = 180
eyes = 'black'
teeth = 'white'
hair = 'black'
one_cm = 2.54
one_pound = 0.45359237


print(f"让我们来谈谈{name}")
print(f"这是我的身高{height}")
print(f"这是我的体重{weight}")
print(f"我的眼睛是{eyes}")
print(f"我的牙齿是{teeth}")
print(f"我的头发是{hair}")
total = age+height+weight
print(f"现在我要将我的年龄{age}我的身高{height}我的体重{weight}加在一起得到{total}")
cm = height * one_cm
si = weight * one_pound

print(f"将英寸转换为厘米得出结果{cm},将磅转换为千克得出结果",round(si))