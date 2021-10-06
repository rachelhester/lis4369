def get_requirements():
    print("Python Looping Structures")
    print("Program Requirements\n")
    print("1. Print while loop.\n")
    print("2. Print for loops using range() function, and implicit and explicit lists.\n")
    print("3. Use break and continue statements.\n")
    print("4. Replicate display below.\n")
    print("Note: In Python, for loop used for iterating over a sequence (i.e., list, tuple, dictionary, set, or string)\n")

def do_loops():
    print("1. while loop")
    counter = 1
    while counter < 4:
        print(counter)
        counter += 1
    print()

    print("2. for loop: using range() function with one arg:")
    for i in range (4):
        print(i)
    print()

    print("3. for loop: using range() function with two args")
    for i in range (0,4):
        print(i)
    print()

    print("4. for loop: using range() function with three args (interval 2)")
    for i in range(1,4,2):
        print(i)
    print()

    print("5. for loop: using range() function with three args (negative interval)")
    for i in range(3,0,-2):
        print(i)
    print()

    print("6. for loop using (implicit) list (i.e., list not assigned to variable)")
    for i in [1,2,3]:
        print(i)
    print()

    print("7. for loop iterating through (explicit) string list")
    states = ["Michigan", "Alabama", "Florida"]
    for state in states:
        print (state)
    print()

    print("8. for loop using break statement (stops loop):")
    for state in states:
        if state == "Alabama":
            break
        print(state)
    print() 

    print("9. for loop using continue statement (stops and continues with next):")
    for state in states:
        if state == "Alabama":
            continue
        print(state)
    print()

    print("10. print list length")
    print(len(states))
    print() 

def main():
    get_requirements()
    do_loops()
main() 

