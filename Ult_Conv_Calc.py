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
        response = input("Do you want to calculate time, mass or measurements?").lower()

        # a list of valid responses
        time_ok = ["time", "t"]
        mass_ok = ["mass", "weight"]
        measure_ok = ["measurements", "measure", "measurement"]

        # checks for valid response and returns text, integer or image
        if response in time_ok:
            return "time"
        elif response in mass_ok:
            return "mass"
        elif response in measure_ok:
            return "measurement"
        elif response == "m":
            choice = input("Press <enter> for mass or any key for measurement: ")
            if choice == "":
                return "mass"
            else:
                return "measurement"
        else:
            # if response is not valid (in the lists), output an error
            print("Sorry, please choose to calculate time, mass or measurements")
            print()


# Main routine
statement_generator("Ultimate Conversion Calculator", "*")
first_time = input("Press <enter> for instructions on how to use the calculator"
                   " otherwise any other key to continue")

keep_going = ""
while keep_going == "":
    if first_time == "":
        instructions()
    calc_choice = user_choice()
    print("You chose", calc_choice)
    print()
    keep_going = input("Press <enter> to continue or any key to stop")
    print()
