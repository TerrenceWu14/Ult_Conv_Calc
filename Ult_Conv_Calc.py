# Functions go here

# Puts a series of symbols at the start and end of text


# Displays instructions for new users


def user_choice():
    valid = False

    while not valid:
        response = input("Do you want to calculate time, mass or measurements?").lower()

        # a list of valid responses
        time_ok = ["time", "t"]
        mass_ok = ["mass", "weight"]
        measure_ok = ["measurement", "measure"]

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
            print(" Sorry, please choose to calculate time, mass or measurements")
            print()


# Main routine
keep_going = ""
while keep_going == "":
    calc_choice = user_choice()
    print("You chose", calc_choice)

