# changing valid answers into unit abbreviation
def to_abbreviation(user_unit, valid_list):
    while True:
        for item in valid_list:
            print("item in list", item)
            if user_unit in item:
                print("possible unit", user_unit)
                return item[0]

        print("oops, you have not chosen a valid unit")
        return "error"


# main routine

distance_list = [
    ["mm", "millimeters", "millimeter"],
    ["cm", "centimeters", "centimeter"],
    ["m", "meters", "meter"],
    ["km", "kilometers", "kilometer"],
]

var_unit = input("Enter Unit")
checked_unit = to_abbreviation(var_unit, distance_list)
print("checked unit", checked_unit)
