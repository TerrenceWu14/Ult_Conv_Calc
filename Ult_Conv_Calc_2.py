# Functions go here

# Checks that the number entered is more than 0
def num_check(question):
    valid = False
    while not valid:
        error = "Please enter a number that is more than zero and lower (or equal to) than 200 (no decimals)"
        try:
            response = int(input(question))
            if response > 0:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


# Puts a series of symbols at the start and end of text
def statement_generator(text, decoration):
    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    print()
    print(statement)
    print()


# Displays instructions for new users
def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose one of the following options to convert:"
          " Measurements, Mass or Time ")
    print("Please only type a number above 0 (with no decimals)")
    print("Complete as many calculations as necessary, "
          "Pressing <enter> at the end of each calculator or any key to quit.")
    print()


# Asks the user if they which calculation they want to do
def user_choice():
    valid = False
    while not valid:
        response = input("Do you want to calculate time, mass, or distance?").lower()
        time_ok = ["time", "t"]
        mass_ok = ["m", "mass", "weight"]
        distance_ok = ["distance", "d"]
        if response in time_ok:
            return "time"
        elif response in mass_ok:
            return "mass"
        elif response in distance_ok:
            return "distance"


# Lists
distance_factors = {
    "cm": 0.01,
    "m": 1,
    "km": 1000,
}

time_factors = {
    "s": 60,
    "m": 1,
    "h": 1/60
}

# Generates heading with *** on both sides
# Asks the user if they want the instructions or not
statement_generator("Ultimate Conversion Calculator", "*")
first_time = input("Press <enter> for instructions on how to use the calculator"
                   " otherwise any other key to continue")

# Main routine
calc_choice = user_choice()
keep_going = ""
while keep_going == "":
    if calc_choice == "distance":
        conv_factors = distance_factors
    elif calc_choice == "time":
        conv_factors = time_factors

    # Asks user what unit they are converting from
    conv_from = input("What do you want to convert from? ").lower()
    if conv_from not in conv_factors:
        print("Invalid input. Please choose from the available units.")
        continue

    what_to_conv = conv_factors[conv_from]

    # Asks user for the value of the unit
    your_num = num_check("Enter the number of what you want to convert (no units): ")

    # Asks user what they are wanting to convert to
    conv_to = input("What do you want to convert to? ").lower()
    if conv_to not in conv_factors:
        print("Invalid input. Please choose from the available units.")
        continue

    # Converts and displays the result
    base = your_num * what_to_conv
    result = base / conv_factors[conv_to]
    print(f"{your_num} {conv_from} is equal to {result} {conv_to}")

    # Ask if the user wants to continue
    keep_going = input("Press Enter to continue or any other key to quit: ")
