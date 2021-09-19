#LIS4369
#Developer: Rachel Hester

#constant
sq_feet_per_acre = 43560

#function for getting requirements
def get_requirements():
    print("Square Feet to Acres")
    print()
    print("Program Requirements:")
    print("1. Research: number of square feet to acre of land.")
    print("2. Must use float data type for user input and calculation.")
    print("3. Format and round conversion to two decimal places.")

def calculate_square_feet():

    #variables
    square_feet = 0.0
    acres = 0.0

    #input
    print("\nInput:")
    square_feet = float(input("Enter square feet: "))
    
    #calculation of square feet to acres
    acres = square_feet / sq_feet_per_acre 


    #print the number of acres but formatted
    print("\nOutput:")
    print("{0:,.2f} square feet = {1:,.2f} acres".format(square_feet, acres))
    

def main():
    get_requirements()
    calculate_square_feet()
main()