# Functions go here

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
def calc(distance):
    distance_desc = {
        "centimeters to kilometers": "{} centimeters is equal to {} kilometers",
        "centimeters to meters": "{} centimeters is equal to {} meters",
        "meters to kilometgithers": "{} meters is equal to {} kilometers",
        "meters to centimeters": "{} meters is equal to {} centimeters",
        "kilometers to meters": "{} kilometers is equal to {} meters",
        "kilometers to centimeters": "{} kilometers is equal to {} centimeters",
    }

    conversion_factors = {
        "centimeters to kilometers": 0.00001,
        "centimeters to meters": 0.01,
        "meters to kilometers": 0.001,
        "meters to centimeters": 100,
        "kilometers to meters": 1000,
        "kilometers to centimeters": 100000,
    }

    while True:
        your_num = float(input("Enter a positive number: "))
        if your_num <= 0:
            print("Please enter a positive number greater than zero.")
        else:
            break

    while True:
        to_do = input(
            "What do you want to convert from and to? ").lower()
        if to_do in conversion_factors:
            multiply_by = conversion_factors[to_do]
            answer = your_num * multiply_by
            conversion_description = conversion_factors.get(to_do, "Unknown conversion")
            print(f"{conversion_description.format(your_num, answer)}")
            break  # Exit the loop if a valid conversion choice is made
        else:
            print("Invalid conversion choice. Please choose a valid option.")


# Main routine

# Generates heading with *** on both sides
# Asks user if they want the instructions or not
statement_generator("Ultimate Conversion Calculator", "*")
first_time = input("Press <enter> for instructions on how to use the calculator"
                   " otherwise any other key to continue")
