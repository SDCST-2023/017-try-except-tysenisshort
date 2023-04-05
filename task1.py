#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with a while loop along with a try...except 
# block so that the user will keep entering in a number
# until they have entered a value integer value
number1 = 0
number = 0
while True:
    try:
        number = input("Please enter in an integer value: ")
        number1 = int(number)
        print(f"your number is {number1}")
        break
    except:
        print("Not a number try again")
