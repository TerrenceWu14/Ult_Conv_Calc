import re

conv_factors = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,

}

to_convert = input("What do you want to convert? (e.g. 10m to cm or 10m - cm) ")  # Your variable holding the string
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
    amount = match.group(1)
    from_unit = match.group(2)
    to_unit = match.group(3)

    print("Amount:", amount)
    print("From:", from_unit)
    print("To:", to_unit)
else:
    print("Pattern not found.")

to_meters = float(amount) / conv_factors[to_unit]

print(f" 1 meter = {to_meters}")
# from_factor = conv_factors[]
# to_factor = conv_factors[to_unit]
#
# result = from_factor * to_factor
#
#
# print(result)

