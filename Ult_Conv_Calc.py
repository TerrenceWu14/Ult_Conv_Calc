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
        mass_ok = ["mass", "weight"]
        measure_ok = ["measurements", "measure", "measurement"]

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


# Main routine
statement_generator("Ultimate Conversion Calculator", "*")
first_time = input("Press <enter> for instructions on how to use the calculator"
                   " otherwise any other key to continue")
keep_going = ""
while keep_going == "":
    calc_choice = user_choice()
    conversion_description = {
        "seconds to minutes": "{} seconds is equal to {} minutes",
        "seconds to hours": "{} seconds is equal to {} hours",
        "minutes to hours": "{} minutes is equal to {} hours",
        "minutes to seconds": "{} minutes is equal to {} seconds",
        "hours to minutes": "{} hours is equal to {} minutes",
        "hours to seconds": "{} hours is equal to {} seconds",
    }
    if calc_choice == "measurement":
        my_dict = {
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
                "Centimeters to Meters, Meters to Kilometers, or Centimeters to Kilometers? (or vice versa)").lower()
            if to_do in my_dict:
                multiply_by = my_dict[to_do]
                answer = your_num * multiply_by
                rounded_answer = round(answer, 2)
                conversion_description = conversion_description.get(to_do, "Unknown conversion")
                print(f"{conversion_description.format(your_num, answer)}")
                break  # Exit the loop if a valid conversion choice is made
            else:
                print("Invalid conversion choice. Please choose a valid option.")

    elif calc_choice == "mass":
        my_dict = {
            "milligrams to grams": 0.001,
            "milligrams to kilograms": 0.000001,
            "grams to milligrams": 1000,
            "grams to kilograms": 0.001,
            "kilograms to grams": 1000,
            "kilograms to milligrams": 1000000,
        }

        while True:
            your_num = float(input("Enter a positive number: "))
            if your_num <= 0:
                print("Please enter a positive number greater than zero.")
            else:
                break

        while True:
            to_do = input(
                "Milligrams to Grams, Grams to Kilograms (or to milligrams) "
                "or Kilograms to Milligrams or Grams").lower()
            if to_do in my_dict:
                multiply_by = my_dict[to_do]
                answer = your_num * multiply_by
                rounded_answer = round(answer, 2)
                conversion_description = conversion_description.get(to_do, "Unknown conversion")
                print(f"{conversion_description.format(your_num, answer)}")
                break  # Exit the loop if a valid conversion choice is made
            else:
                print("Invalid conversion choice. Please choose a valid option.")

    elif calc_choice == "time":
        my_dict = {
            "seconds to minutes": 0.01666666666,
            "seconds to hours": 0.00027777777,
            "minutes to hours": 0.01666666666,
            "minutes to seconds": 60,
            "hours to minutes": 60,
            "hours to seconds": 3600,
        }

        while True:
            your_num = float(input("Enter a positive number: "))
            if your_num <= 0:
                print("Please enter a positive number greater than zero.")
            else:
                break

        while True:
            to_do = input(
                "Seconds to Minutes, Minutes to Hours or Hours to (Minutes/Hours)").lower()
            if to_do in my_dict:
                multiply_by = my_dict[to_do]
                answer = your_num * multiply_by
                conversion_description = conversion_description.get(to_do, "Unknown conversion")
                print(f"{conversion_description.format(your_num, answer)}")
                break  # Exit the loop if a valid conversion choice is made
            else:
                print("Invalid conversion choice. Please choose a valid option.")

    print()
    keep_going = input("Press <enter> to continue or any key to stop")
    print()
