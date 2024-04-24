#a function that takes two argument and return a formated string
def func (a,b):
    result= " a number {} and a string '{}'.".format(a,b)
    return result

print(func(145,"o"))

#function to calculate area of a pond in square meter
def calculate_area_of_a_pond (radius,pi):
    area_of_a_pond = pi * radius ** 2
    return area_of_a_pond
print("{} square meters".format(calculate_area_of_a_pond(84,3.14)))

#function to calculate the total water in a pond
def calculate_total_water_in_a_pond (area_of_the_pond,water_per_square_meter):
    total_water_in_a_pond = area_of_the_pond * water_per_square_meter
    return "{} litres".format(int(total_water_in_a_pond))
print(calculate_total_water_in_a_pond(calculate_area_of_a_pond(84,3.14), 1.4))

#Function to Calculate Speed in metre/second
def calculate_speed (distance,time_in_minutes):
    time_in_sec= time_in_minutes * 60
    speed = distance / time_in_sec
    return "{} m/s".format(int(speed))
print(calculate_speed(490,7))