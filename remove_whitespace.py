
# import re
# to_convert = input("What do you want to convert? ")
# x = re.sub(" to ", "-", to_convert)
# x = re.sub(" ", "", x)
# print(x)

import re

to_convert = input("What do you want to convert? ")  # Your variable holding the string
# Turns "to" into a "-"
x = re.sub(" to ", "-", to_convert)
# Removes whitespaces
x = re.sub(" ", "", x)
# Define the regex pattern to capture the amount, 'from' unit, and 'to' unit
pattern = r'^(\d+)([a-zA-Z]+)-([a-zA-Z]+)$'

# Match the pattern in the input string
match = re.match(pattern, x)

if match:
    amount = match.group(1)
    from_unit = match.group(2)
    to_unit = match.group(3)

    print("Amount:", amount)
    print("From:", from_unit)
    print("To:", to_unit)
else:
    print("Pattern not found.")


