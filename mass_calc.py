def num_check(question):
    # Checks if the user entered a positive integer between 1 and 200
    while True:
        try:
            response = int(input(question))
            if 1 <= response <= 200:
                return response
            else:
                print("Please enter a number between 1 and 200 (inclusive).")
        except ValueError:
            print("Please enter a valid integer.")


