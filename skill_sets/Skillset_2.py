#LIS4369
#Developer: Rachel Hester

#function for getting requirements
def get_requirements():
    print("Miles Per Gallon")
    print()
    print("Program Requirements:")
    print("1. Convert MPG")
    print("2. Must use float data type for user input and calculation")
    print("3. Format and round conversion to two decimal places.")

def calculate_miles_per_gallon():

    print("\nInput:")
    miles_driven = float(input("Enter miles driven: "))
    gallons = float(input("Enter gallons of fuel used: "))


    mpg = miles_driven / gallons 

    print("\nOutput:")
    print("{0:,.2f} miles driven and {1:,.2f} gallons used = {2:,.2f} mpg".format(miles_driven, gallons, mpg))
def main():
    get_requirements()
    calculate_miles_per_gallon()
main()