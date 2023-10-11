# Functions go here

# Try to go to a base value e.g. distance base value would be meters,
# Go to meters first by timing the number by 0.01 and then convert from there

# Checks that the number entered is more than 0
def num_check(question1: object):
    # checks if the user entered a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero and lower (or equal to) than 200 (no decimals)"

        try:

            # asks user to enter a number
            response: int = int(input(question1))

            # checks if a number is above zero
            if response > 0:
                return response

            # Outputs error if number is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Puts a series of symbols at the start and end of text
def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


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
    return ""


# Asks the user if they which calculation they want to do
def user_choice():
    valid = False

    while not valid:
        response = input("Do you want to calculate time, mass, or measurements?").lower()

        time_ok = ["time", "t"]
        mass_ok = ["m", "mass", "weight"]
        distance_ok = ["distance, d"]

        if response in time_ok:
            return "time"
        elif response in mass_ok:
            return "mass"
        elif response in distance_ok:
            return "distance"


# Calculates distance
def distance():
    conversion_data = {
        "centimeters to kilometers": {"factor": 0.00001, "description": "{} centimeters is equal to {} kilometers"},
        "centimeters to meters": {"factor": 0.01, "description": "{} centimeters is equal to {} meters"},
        "meters to kilometers": {"factor": 0.001, "description": "{} meters is equal to {} kilometers"},
        "meters to centimeters": {"factor": 100, "description": "{} meters is equal to {} centimeters"},
        "kilometers to meters": {"factor": 1000, "description": "{} kilometers is equal to {} meters"},
        "kilometers to centimeters": {"factor": 100000, "description": "{} kilometers is equal to {} centimeters"},
    }

    while True:
        your_num = float(input("Enter a positive number: "))
        if your_num <= 0:
            print("Please enter a positive number greater than zero.")
        else:
            break

    while True:
        to_do = input("What do you want to convert from and to? ").lower()
        if to_do in conversion_data:
            conversion_info = conversion_data[to_do]
            multiply_by = conversion_info["factor"]
            description = conversion_info["description"]
            answer = your_num * multiply_by
            print(f"{description.format(your_num, answer)}")
            break  # Exit the loop if a valid conversion choice is made
        else:
            print("Invalid conversion choice. Please choose a valid option.")


# Generates heading with *** on both sides
# Asks user if they want the instructions or not
statement_generator("Ultimate Conversion Calculator", "*")
first_time = input("Press <enter> for instructions on how to use the calculator"
                   " otherwise any other key to continue")
# Main routine
distance()
