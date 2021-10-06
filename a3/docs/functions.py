def get_requirements():
    print("Painting Estimator\n")
    print("Program Requirements:")
    print("1. Calculate home interior paint cost (w/o primer)")
    print("2. Must use float data types.")
    print("3. Must use SQFT_PER_GALLON constant (350)")
    print("4. Must use iteration structure (aka \"/loop\"/")
    print("5. Format, right-align numbers, and round to two decimal places.")
    print("6. Create at least five functions that are called by the program:")
    print("\t a. main(): calls two other functions: get_requirements() and estimate_painting_cost()")
    print("\t b. get_requirements(): displays the program requirements")
    print("\t c. estimate_painting_cost(): calculates interior home painting, and calls print functions")
    print("\t d. print_painting_estimate(): displays painting costs")
    print("\t e. print_painting_percentage(): displays painting costs percentages")

def estimate_painting_cost():
    SQFT_PER_GALLON = 350
    print("\nInput:")
    interior_total = float(input("Enter total interior sq ft: "))
    price_per_gallon = float(input("Enter price per gallon paint: "))
    hourly_rate = float(input("Enter hourly painting rate per sq ft: "))

    number_of_gallons = interior_total / SQFT_PER_GALLON
    cost_of_paint = number_of_gallons * price_per_gallon 
    cost_of_labor = interior_total * hourly_rate 

    total_cost = cost_of_paint + cost_of_labor
    paint_percentage = cost_of_paint / total_cost * 100
    labor_percentage = cost_of_labor / total_cost * 100
    total_percentage = paint_percentage + labor_percentage 

    print_painting_estimate(interior_total, SQFT_PER_GALLON, number_of_gallons, price_per_gallon, hourly_rate)
    print_painting_percentage(cost_of_paint, cost_of_labor, total_cost, paint_percentage, labor_percentage, total_percentage)

    print()
    cont = input("Estimate another paint job? (y/n): ")
    while cont.lower() in ['y', 'n']:
        if cont == 'y':
            estimate_painting_cost()
            break
        if cont == 'n':
            print()
            print("Thank you for using our Paint Estimator!\n\n")
            print("Please see our website: http://rachelhester.com")
            break

def print_painting_estimate(interior_total, SQ_FT_PER_GALLON, number_of_gallons, price_per_gallon, hourly_rate):
    print("\nOutput:")
    print("{0:<10} {1:>20}".format("Item", "Amount"))
    print("{0:<10} {1:>18,.2f}".format("Total Sq Ft:", interior_total))
    print("{0:<10} {1:>13,.2f}".format("Sq Ft per Gallon:", SQ_FT_PER_GALLON))
    print("{0:<10} {1:>12,.2f}".format("Number of Gallons:", number_of_gallons))
    print("{0:<10}      ${1:>8,.2f}".format("Paint per Gallon:", price_per_gallon))
    print("{0:<10}       ${1:>8,.2f}".format("Labor per Sq Ft:", hourly_rate))

def print_painting_percentage(cost_of_paint, cost_of_labor, total_cost, paint_percentage, labor_percentage, total_percentage):
    print("{0:<9} {1:>10} {2:>14}".format("\nCost", "Amount", "Percentage"))
    print("{0:<9} ${1:>8,.2f} {2:>13,.2f}%".format("Paint:", cost_of_paint, paint_percentage))
    print("{0:<9} ${1:>4,.2f} {2:>13,.2f}%".format("Labor:", cost_of_labor, labor_percentage))
    print("{0:<9} ${1:>4,.2f} {2:>13,.2f}%".format("Total:", total_cost, total_percentage))


