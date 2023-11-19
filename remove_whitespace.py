import re


# Checks that the number entered is more than 0
def num_check(question):
    valid = False
    while not valid:
        error = "Please enter a number that is more than zero (no decimals)"
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


keep_going = ""
while keep_going == "":
    statement_generator("Ultimate Conversion Calculator", "*")
    first_time = input("Press <enter> for instructions on how to use the calculator"
                       " otherwise any other key to continue")
    if first_time == "":
        instructions()

    distance_factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
    }
    time_factors = {
        "s": 60,
        "m": 1,
        "h": 1 / 60,
    }

    mass_factors = {
        "mg": 1000,
        "g": 1,
        "kg": 1000,
    }

    to_convert = input("What do you want to convert? (e.g. 10m to cm or 10m - cm) ")
    if to_convert == ""
    # Turns "to" into a "-"
    x = re.sub(" to ", "-", to_convert)
    # Removes whitespaces
    x = re.sub(" ", "", x)
    # Define the regex pattern to capture the amount, 'from' unit, and 'to' unit
    pattern = r'^(\d+)([a-zA-Z]+)-([a-zA-Z]+)$'
    # Match the pattern in the input string
    match = re.match(pattern, x)
    # Puts the matches into groups
    if match:
        amount = float(match.group(1))
        from_unit = match.group(2)
        to_unit = match.group(3)

        print("Amount:", amount)
        print("From:", from_unit)
        print("To:", to_unit)
    else:
        print("Pattern not found.")

    # to_meters = float(amount) / conv_factors[to_unit]

    # print(f" 1 meter = {to_meters}")
    # Converts and prints result
    result = amount * conv_factors[from_unit] / conv_factors[to_unit]
    print(f"{amount}{from_unit} is equal to {result}{to_unit}")

    # Ask if the user wants to continue
    keep_going = input("Press Enter to continue or any other key to quit: ")
