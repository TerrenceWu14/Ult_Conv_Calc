# def remove_spaces(user_input):
#     return user_input.replace(" ", "")
#
#
# ask = input("What do you want to convert? ")
# to_convert = remove_spaces(ask)
# print(to_convert)

import re
to_factor = input("What do you want to convert? ")
x = re.sub("\s", "-", to_factor)
print(x)
