# This is the number of cars
cars = 100
# This is the capacity for each car
space_in_a_car = 4
# This is the number of drivers
drivers = 30
# This is the number of passengers for the cars
passengers = 90
# This is how many cars will not be driven, as they don't have a driver
cars_not_driven = cars - drivers
# This is the number of cars driven
cars_driven = drivers
# This is the number of people that can fit in the cars based on how many will be driven
carpool_capacity = cars_driven * space_in_a_car
# This is how many people will need to be in each car based on the number of people and the number of cars that will be driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "Cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")