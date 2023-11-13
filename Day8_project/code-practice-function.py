######## Using this file to follow along with bit-size function practice exercises in the course ###########

# definiting function with two inputs
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Nifemi", "Boston")

#defining functions with keyword arguments
# def greet_with(name="Nifemi", location="Boston"):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with(location="New York", name="Omolola")

#function to calculate number of cans needed to paint a wall
# import math
# def paint_estimator(height, width, coverage):
#     cans = (height * width) / coverage
#     cans = math.ceil(cans)
#     print(f"You'll need {cans} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 10

# paint_estimator(height=test_h, width=test_w, coverage=coverage)


#function to check for prime numbers
def prime_checker(number):
    is_prime = True
    for m in range(2, number):
        if number % m == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

num = int(input("Check this number: "))
prime_checker(number=num)
