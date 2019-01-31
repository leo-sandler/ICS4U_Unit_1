import os
import random
# Task 1: Create a function that takes 2 numbers and returns True if their product is greater than 25.


def greater_than(num1, num2):
    if (int(num1) * int(num2)) > 25:
        return True
    else:
        return "Not greater than 25"


print(greater_than(5, 5))
print(greater_than(5, 6))

# Task 2: Create a file using open() and then write every odd number between 1-10 on separate lines in the file.

try:
    os.chdir("Lesson 1.1")
    newfile = open("odd_nums.txt", "x")
    for number in range(0, 10):
        if number % 2 != 0:
            newfile.write(str(number + str("\n")))
    newfile.close()
except:  # Yes, it is a bare except PEP 8.
    print("Already written out")


# Task 3: Create a function that reads the file in 2. and returns the sum of all the numbers.
reading = open("odd_nums.txt", "r")
reading.seek(0)
reader = reading.readlines()
var_sum = 0
for x in reader:
    var_sum += int(x)
print(var_sum)


# Task 4:  Create a function that writes a random number to a file, asks the user to guess a number, and then checks
# if the user guessed the correct number by reading the file.
def random_number():
    user_input = input(str("Enter the number: "))
    num_file = open("number.txt", "r+")
    num_file.write(str(random.randint(0, 10)))
    if user_input == num_file.readlines():
        print("Correct")
    else:
        print("Incorrect")
    open('number.txt', 'w').close()  # Clearing


random_number()
