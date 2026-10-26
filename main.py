"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return (annual_cost / 2)


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (CLASS_DAYS_PER_SEMESTER * 2)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost / (credits * 2)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (cost_per_credit(annual_cost, credits) * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER

def cost_per_skipped_class(annual_cost, classes_skipped, credits):
    return(cost_per_class(annual_cost, credits) * classes_skipped)

def show_menu():
    print(f"\n")
    print(" THE COST OF COLLEGE \n" \
    "   1 Per semester\n" \
    "   2 Per month\n" \
    "   3 Per class day\n" \
    "   4 Per credit\n" \
    "   5 Per CS 1430 class\n" \
    "   6 Cost of skipped classes\n" \
    "   Q quit")

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.

    total_cost = float(input("Total cost for one year: "))
    credits = float(input("Credits this semester: "))

    while True:
        # Show your menu here.
        """I know it says show your menu here, but wouldn't it show with every loop then? It'd be a lot cleaner outside the loop."""
        show_menu()#I just prefer it being moved.

        choice = input("Choose an option: ")
        if choice == "1":
            print(f"{cost_per_semester(total_cost):.2f}")
        if choice == "2":
            print(f"{cost_per_month(total_cost):.2f}")
        if choice == "3":
            print(f"{cost_per_day(total_cost):.2f}")
        if choice == "4":
            print(f"{cost_per_credit(total_cost, credits):.2f}")
        if choice == "5":
            print(f"{cost_per_class(total_cost, credits):.2f}")
        if choice == "6":
            classes_skipped=int(input("How many classes skipped?"))
            print(f"{cost_per_skipped_class(total_cost, classes_skipped, credits):.2f}")

        if choice == "Q" or choice == "q":
            print("Thanks for running the numbers!")
            break

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
