people = 30
cars = 40
trucks = 15


if cars > people:
    print("我们应该开车去")
elif cars < people:
    print("我们不应该开车去")
else:
    print("我们无法决定")

if trucks > cars:
    print("卡车太多了")
elif trucks < cars:
    print("或许我们可以坐卡车")
else:
    print("我们无法做决定")

if people > trucks:
    print("好吧，让我们就坐卡车去吧")
else:
    print("好吧，那我们就呆在家里")

if cars > people or trucks <cars:
    print("我们应该开卡车去")
else:
    print("我们呆在家里")