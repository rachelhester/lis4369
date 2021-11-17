#Developer: Rachel Hester
#Class: LIS4369
import math

def get_requirements():
    print("\nSphere Volume Program")
    print()
    print("Program Requirements:")
    print("1. Program calculates sphere volume in liquid U.S. gallons from user-entered diameter value in inches, and rounds to two decimal places.")
    print("2. Must use Python's *built-in* PI and pow() capabilities.")
    print("3. Program checks for non-integers and non-numeric values.")
    print("4. Program continues to prompt for user entry until no longer requested, prompt accepts upper or lower case letters.")
    print()

def get_volume():
    CUBIC_INCHES_TO_GALLON = 231
    choice = ''

    while True:
        print("Input:")
        choice = input("Do you want to calculate a sphere volume (y or n)? ").lower()
    
        print("\nOutput:")

        while(choice == 'y'):

            diameter = input("Please enter diameter in inches (integers only): ")
            if (diameter.isnumeric()):
            #doMaTH

                radius = int(diameter) / 2
                volume = (4/3) * math.pi * (pow(radius,3))
                volume = volume / CUBIC_INCHES_TO_GALLON
                print("\nSphere volume: " + str(round(volume,2)) + " liquid U.S. gallons.")

                choice = str(input("\nDo you want to convert another sphere volume? ")).lower()


            else:
                print("\nNot valid integer!")
        else:
            print("\nThank you for using our Sphere Volume Calculator!")
            break
def main():
    get_requirements()
    get_volume()
main()

