from random import random  # Importing a pseudo-random number generator module

my_random_number = random() * 100

if my_random_number > 50:
    print(my_random_number)
else:
    print("Too small!")

# this can be written in one line as below
print(my_random_number) if my_random_number > 50 else print("Too small")
