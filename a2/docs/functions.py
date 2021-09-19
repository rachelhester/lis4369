#LIS4369
#Developer: Rachel Hester

#function for getting requirements
def get_requirements():
    print("Payroll Calculator")
    print()
    print("Program Requirements:")
    print("1. Must use float data type for user input.")
    print("2. Overtime rate: 1.5 times hourly rate (hours over 40).")
    print("3. Holiday rate: 2.0 times hourly rate (all holiday hours)")
    print("4. Must format currency with dollar sign, and round to two decimal places.")
    print("5. Create at least three functions that are called by the program:")
    print("\t a. main(): calls at least two other functions.")
    print("\t b. get_requirements(): displays the program requirements.")
    print("\t c. calculate_payroll(): calculates an individual one-week paycheck.")

def calculate_hours():

    #variables given
    base_hours = 40
    overtime_rate = 1.5
    holiday_rate = 2.0

    #input 
    print("\nInput:")
    hours = float(input("Enter hours worked: "))
    holiday_hours = float(input("Enter holiday hours: "))
    hourly_pay = float(input("Enter hourly pay rate: "))

    #math to calculate pay rates
    base_pay = base_hours * hourly_pay
    overtime_hours = hours - base_hours 

    #if statement
    if hours > base_hours:

        #overtime calculation
        overtime_pay = overtime_hours * hourly_pay * overtime_rate 

        #holiday calculation
        holiday_pay = holiday_hours * hourly_pay * holiday_rate 

        #calculate total gross pay
        total_pay = base_hours * hourly_pay + overtime_pay + holiday_pay 

    else:
        #calculate total pay without overtime but include holiday work
        overtime_pay = 0
        holiday_pay = holiday_hours * hourly_pay * holiday_rate 
        total_pay = base_hours * hourly_pay + holiday_pay 
    
        
    #output
    print("\nOutput:")
    print("{0:<10} ${1:,.2f}".format('Base:', base_pay))
    print("{0:<10} ${1:,.2f}".format('Overtime:', overtime_pay))
    print("{0:<10} ${1:,.2f}".format('Holiday:', holiday_pay))
    print("{0:<10} ${1:,.2f}".format('Total/Gross:', total_pay))

