# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
#allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for candy in candy_list:
    print("[" + f"{(candy_list.index(candy))}" + "]" + candy)

# Run through a loop which allows the user to choose which candies to take home wiht them
for x in range(len(candy_list)):
    selected = input("Which candy would you like to bring home?")

    # Add the candy at the index chosen to the candy cart list
    candy_cart.append(candy_list[int(selected)])
    
# Loop through the candy cart to say what candies were brought home
print("I brought home with me ...")
for candy in candy_cart:
    print(candy)
