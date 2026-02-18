print("Car Rental")
cars = ["Sedan","SUV","Mini"]
rent = 1000
car = input("Enter car type: ")
days = input("Enter days: ")
if car in car:
    total = days * rent
else:
    print("Car not available")
tax = total * 0.1
amount = total + tax
print("Car:", car)
print("Amount:", amount)
for i in range(3):
    print("Thank you")

print("End")
