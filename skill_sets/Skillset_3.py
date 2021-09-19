#LIS4369
#Developer: Rachel Hester

#function for getting requirements
def get_requirements():
    print("IT/ICT Student Percentage")
    print()
    print("Program Requirements:")
    print("1. Find number of IT/ICT students in class")
    print("2. Calculate IT/ICT Student Percentage.")
    print("2. Must use float data type (to facilitate right-alignment)")
    print("3. Format, right-align numbers, and round to two decimal places.")

def calculate_percentage():
    #input 
    print("\nInput:")
    it = float(input("Enter number of IT students: "))
    ict = float(input("Enter number of ICT students: "))

    #math to calculate percentages
    total = it + ict
    it_percentage = it / total * 100
    ict_percentage = ict / total * 100

    #output
    print("\nOutput:")
    print("Total students: {0:,.2f} \nIT Students: {1:,.2f}% \nICT Students: {2:,.2f}% ".format(total, it_percentage, ict_percentage))

def main():
    get_requirements()
    calculate_percentage()
main()