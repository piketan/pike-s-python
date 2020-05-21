def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"你有{cheese_count}种奶酪")
    print(f"你有{boxes_of_crackers}盒饼干")

print("可以直接给函数赋值")
cheese_and_crackers(20,30)

print("可以用变量给函数赋值")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("我们也可以在函数里数学计算")
cheese_and_crackers(10+100,900+98)

print("我们也可以结合将变量和数学计算结合起来")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)