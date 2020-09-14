name = input("Enter name  - ")
year = int(input("Enter Birth Year  - "))
age = 2020 - year
response = input("Press Y for Printing and N for cancelling - ")
if response == "N" or response == "n":
    print("No actions taken as User selected N")
    print("Thanks for using")
if response == "Y" or response == "y":
    print(name, "Your age is",age)
    print("Thanks for using")
else:
    print("User entered inappropriate data")
    print("Thanks for using")
