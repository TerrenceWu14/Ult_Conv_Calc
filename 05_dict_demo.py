my_dict = {
    "meters to kilometers": 0.001,
    "meters to centimeters": 100,
}

your_num = int(input("Enter the length (in meters): "))
to_do = input("meters to kilometers or meters to centimeters?").lower()

# looks up the value
multiply_by = my_dict[to_do]
# do math!
answer = your_num * multiply_by
print("{} x {} = {}".format(your_num, multiply_by, answer))
