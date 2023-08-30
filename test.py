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
            your_num = int(input("Enter the amount of time (in minutes): "))
        elif response in mass_ok:
            your_num = int(input("Enter the mass (in kilograms): "))
        elif response in measure_ok:
            your_num = int(input("Enter the length (in meters): "))
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