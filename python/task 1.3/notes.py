# first_name = input("Enter the first name: ")
# last_name = input("Enter the last name: ")
# first_name = first_name.capitalize()
# last_name = last_name.capitalize()
# print("Your name is", first_name, last_name)

# ---------------
# a = int(input("enter a number: "))
# b = int(input("enter a different number to be added to the first number: "))

# ---------------
# print("Sum of inputs: " + str(a+b))


# ---------------
# pets = ['Dog', 'Iguana', 'Cat', 'Snake', 'Turtle']

# for i in range(0, 3):
#     print(pets[i])

# ---------------
# num = int(input("Enter a number to be divided: "))
# start = int(input("Enter a starting point for the divisor: "))
# end = int(input("Enter an end point for the divisor: "))


# ---------------
# for div in range(start, end):
#     if div == 0:
#         print("Division by zero, skipping to next value.")
#         continue
#     print(num / div)

# ---------------
# fruits = ['Apples', 'Oranges', 'Bananas']
# count = 0

# for element in fruits:
#     print("Item " + str(count) + ": " + element)
#     count += 1


# fruits = ['Apples', 'Oranges', 'Bananas']
# for position, value in enumerate(fruits):
#     print("Item " + str(position) + ": " + value)

# ---------------
# def adder(value1, value2):
#     result = value1 + value2
#     print("The added result is " + str(result))

# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))
# adder(a, b)

# ---------------
# def divider(value1, value2):
#     print(value1 / value2)

# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))

# divider(a, b)
# divider(value1 = a, value2 = b)


# ---------------
# text = "I like apples"

# def my_func():
#     global text
#     # We'll try joining another string to 'text'
#     text = text + "... but I love oranges better!"
#     print("text from the inside: " + text)

# my_func()
# print("text from the outside: " + text)