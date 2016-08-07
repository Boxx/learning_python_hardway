# Total number of cars in the fleet
cars = 100
# Amount of space each car has
space_in_a_car = 4.0
# Number of drivers in our employ
drivers = 30
# Number of passengers that need to ride
passengers = 90
# Cars not able to be driven
cars_not_driven = cars - drivers
# Number of cars we can field
cars_driven = drivers
# Our total capacity for passengers
carpool_capacity = cars_driven * space_in_a_car
# Average amount of passengers in each carpool
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
