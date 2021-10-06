

def get_requirements():
    print("Find calories per grams of fat, carbs, and protein.")
    print("Calculate percentages.")
    print("Must use float data types.")
    print("Format, right-align numbers, and round to two decimal places.")

def calculate_output():
    fat = int(input("Enter total fat grams: "))
    carb = int(input("Enter total carb grams: "))
    protein = int(input("Enter total protein grams: "))
    caloriesfat = fat * 9
    caloriescarb = carb * 4
    caloriesprotein = protein * 4

    totalcalories = caloriesfat + caloriescarb + caloriesprotein
    fatpercent = (caloriesfat/totalcalories)*100
    carbpercent = (caloriescarb/totalcalories)*100
    proteinpercent = (caloriesprotein/totalcalories)*100

    print("\nOutput:")
    print("{0:<12} {1:<12} {2:<12}".format("Type", "Calories", "Percentage"))
    print("{0:<12} {1:<12,.2f} {2:>8.2f} {3}".format("Fat", caloriesfat, fatpercent, "%"))
    print("{0:<12} {1:<12,.2f} {2:>8.2f} {3}".format("Carbs", caloriescarb, carbpercent, "%"))
    print("{0:<12} {1:<12,.2f} {2:>8.2f} {3}".format("Protein", caloriesprotein, proteinpercent, "%"))

def main():
    get_requirements()
    calculate_output()
main() 