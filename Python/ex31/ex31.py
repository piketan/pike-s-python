print("""您在一个有两扇门的黑暗房间。
您需要选择穿过1号门或者2号门？""")

door = input('>')

if door == "1":
    print("这里有只大熊在吃芝士蛋糕")
    print("你要做什么?")
    print("1.拿走蛋糕\n2.对熊尖叫")


    bear = input('>')

    if bear == "1":
        print("熊吃掉了你的脸")
    elif bear == "2":
        print("熊吃掉了你的腿")
    else:
        print("好吧，选择3可能更好")
        print("熊逃跑了")

elif door == "2":
    print("你凝视着克鲁苏眼睛里的无尽深渊")
    print("1.蓝莓")
    print("2.黄色夹克衣")
    print("3.理解左轮手枪的叫声")

    insanity = input('>')

    if insanity == "1" or insanity == "2":
        print("你的身体靠果冻的心生存")
    else:
        print("精神错乱使你的眼睛腐蚀成一滩淤泥")
else:
    print("你跌跌撞撞地倒在刀上死了")
