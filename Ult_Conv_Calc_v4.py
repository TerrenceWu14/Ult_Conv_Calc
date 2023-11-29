import re


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


def to_abbreviation(user_unit, valid_list):
    while True:
        for item in valid_list:
            if user_unit in item:
                return item[0]
        print("oops, you have not chosen a valid unit")
        return "error"


statement_generator("Ultimate Conversion Calculator", "*")
first_time = input("Press <enter> for instructions on how to use the calculator"
                   " otherwise any other key to continue")
if first_time == "":
    instructions()

unit_list = [

    ["mm", "millimeters", "millimeter"],
    ["cm", "centimeters", "centimeter"],
    ["m", "meters", "meter"],
    ["km", "kilometers", "kilometer"],
    ["h", "hours", "hour"],
    ["min", "minutes", "minute"],
    ["s", "seconds", "second"],
    ["kg", "kilograms", "kilogram"],
    ["g", "grams", "gram"],
    ["mg", "milligrams", "milligram"],
]

distance_factors = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
}
time_factors = {
    "s": 1 / 60,
    "min": 1,
    "h": 60,
}

mass_factors = {
    "mg": 1000,
    "g": 1,
    "kg": 1000,
}

conv_factors = ""

keep_going = ""
while keep_going == "":

    to_convert = input("What do you want to convert? (e.g. 10m to cm or 10m-cm or 10 meters to centimeters) ").lower()

    while True:
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
            from_unit = to_abbreviation(from_unit, unit_list)
            to_unit = match.group(3)
            to_unit = to_abbreviation(to_unit, unit_list)
            break
        else:
            print("Please follow the format")

    if from_unit not in conv_factors or to_unit not in conv_factors:
        print("Invalid units. Please choose valid units.")
        continue  # Restart the loop to get valid input

    if from_unit in ["km", "m", 'cm', "mm"]:
        conv_factors = distance_factors
    elif from_unit in ["kg", "g", "mg"]:
        conv_factors = mass_factors
    elif from_unit in ["h", "min", "s"]:
        conv_factors = time_factors
    # Converts and prints result
    result = amount * conv_factors[from_unit] / conv_factors[to_unit]
    print(f"{amount}{from_unit} is equal to {result}{to_unit}")

    # Ask if the user wants to continue
    keep_going = input("Press Enter to continue or any other key to quit: ")
