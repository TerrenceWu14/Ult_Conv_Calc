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

    time_desc = {
        "seconds to minutes": "{} seconds is equal to {} minutes",
        "seconds to hours": "{} seconds is equal to {} hours",
        "minutes to hours": "{} minutes is equal to {} hours",
        "minutes to seconds": "{} minutes is equal to {} seconds",
        "hours to minutes": "{} hours is equal to {} minutes",
        "hours to seconds": "{} hours is equal to {} seconds",
    }
    mass_desc = {
        "milligrams to grams": "{} milligrams is equal to {} grams",
        "milligrams to kilograms": "{} milligrams is equal to {} kilograms",
        "grams to milligrams": "{} grams is equal to {} milligrams",
        "grams to kilograms": "{} grams is equal to {} kilograms",
        "kilograms to grams": "{} kilograms is equal to {} grams",
        "kilograms to milligrams": "{} kilograms is equal to {} milligrams",
    }

# Loop to allow multiple calculations
keep_going = ""
while keep_going == "":
    conversion_description = {
        "seconds to minutes": "{} seconds is equal to {} minutes",
        "seconds to hours": "{} seconds is equal to {} hours",
        "minutes to hours": "{} minutes is equal to {} hours",
        "minutes to seconds": "{} minutes is equal to {} seconds",
        "hours to minutes": "{} hours is equal to {} minutes",
        "hours to seconds": "{} hours is equal to {} seconds",
        "milligrams to grams": "{} milligrams is equal to {} grams",
        "milligrams to kilograms": "{} milligrams is equal to {} kilograms",
        "grams to milligrams": "{} grams is equal to {} milligrams",
        "grams to kilograms": "{} grams is equal to {} kilograms",
        "kilograms to grams": "{} kilograms is equal to {} grams",
        "kilograms to milligrams": "{} kilograms is equal to {} milligrams",
        "centimeters to kilometers": "{} centimeters is equal to {} kilometers",
        "centimeters to meters": "{} centimeters is equal to {} meters",
        "meters to kilometers": "{} meters is equal to {} kilometers",
        "meters to centimeters": "{} meters is equal to {} centimeters",
        "kilometers to meters": "{} kilometers is equal to {} meters",
        "kilometers to centimeters": "{} kilometers is equal to {} centimeters",
    }
    # Calculations for Measurement
    calc_choice = user_choice()
    if calc_choice == "measurement":
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
                rounded_answer = round(answer, 2)
                conversion_description = conversion_description.get(to_do, "Unknown conversion")
                print(f"{conversion_description.format(your_num, answer)}")
                break  # Exit the loop if a valid conversion choice is made
            else:
                print("Invalid conversion choice. Please choose a valid option.")

    elif calc_choice == "mass":
        conversion_factors = {
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
                "What do you want to convert from and to? ").lower()
            if to_do in conversion_factors:
                multiply_by = conversion_factors[to_do]
                answer = your_num * multiply_by
                rounded_answer = round(answer, 2)
                conversion_description = conversion_description.get(to_do, "Unknown conversion")
                print(f"{conversion_description.format(your_num, answer)}")
                break  # Exit the loop if a valid conversion choice is made
            else:
                print("Invalid conversion choice. Please choose a valid option.")

    elif calc_choice == "time":
        conversion_factors = {
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
                "What do you want to convert from and to? ").lower()
            if to_do in conversion_factors:
                multiply_by = conversion_factors[to_do]
                answer = your_num * multiply_by
                conversion_description = conversion_description.get(to_do, "Unknown conversion")
                print(f"{conversion_description.format(your_num, answer)}")
                break  # Exit the loop if a valid conversion choice is made
            else:
                print("Invalid conversion choice. Please choose a valid option.")