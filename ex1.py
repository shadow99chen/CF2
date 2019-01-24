#对cars赋值

cars = 100

#对spase_in_a_car赋值

space_in_a_car = 4.0

#对drivers赋值

drivers = 30

#对pasengers赋值

pasengers = 90
#对cars_not_driven赋值

cars_not_driven = cars - drivers

#对cars_driven赋值

cars_driven = drivers

#对carpool_capacity赋值

carpool_capacity = cars_driven * space_in_a_car

#对average_passengers_per_car赋值

average_passengers_per_car = pasengers / cars_driven

#输出可提供的车辆数目

print("There are",cars,"cars available.")

#输出可供使用的司机人数

print("There are only",drivers,"drivers available.")

#输出空车辆的数目

print("There will be",cars_not_driven,"empty cars today.")

#输出能运输的总人数

print("We can transport",carpool_capacity,"people today.")

#输出我们需要运输总人数

print("We have",pasengers,"to carpool today.")

#输出我们每车平均需要装载的人数
print("We need to put about",average_passengers_per_car,"in each car.")
