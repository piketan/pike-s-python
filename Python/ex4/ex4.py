cars = 100
#给cars一个变量100
space_in_a_car = 4.0
#给space_in_a_car一个变量4.0
space_in_a_cars = 4
#变量如果有浮点数的话计算结果也会有浮点数
drivers = 30
#给drivers一个变量30
passengers = 90
#给passengers一个变量90
cars_not_driven = cars - drivers
#给cars - drivers cars的变量100-drivers的变量30
cars_driven = drivers
#给cars_driven一个drivers的变量
carpool_capacity = cars_driven * space_in_a_car
carpool_capacitys = cars_driven * space_in_a_cars
average_passengers_per_car = passengers / cars_driven

print("今天有",cars,"辆车")
print("但是只有",drivers,"个司机")
print("所以今天将有",cars_not_driven,"辆车没有司机")
print("今天可以运输",carpool_capacity,"个人")
print("今天可以运输",carpool_capacitys,"个人")
print("我们今天有",passengers,"人拼车")
print("每辆车需要有",average_passengers_per_car,"个人坐在车上")
#一个=的作用是赋值两个等号==的作用是等于的意思