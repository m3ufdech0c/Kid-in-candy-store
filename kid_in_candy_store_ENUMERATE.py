# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]
for i, candy in enumerate(candy_list):
  print(f"[{i}] {candy}")
# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

while allowance > 0:
  choice = input("Which candy do you want to buy? ")
  candy_cart.append(candy_list.pop(int(choice)))
  allowance -= 1
  print("Cart:")
  
  # Print out options
  print(candy_cart)