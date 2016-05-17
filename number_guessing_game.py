import random

user_guess = int(input("Please enter a number: "))
numbers = (range(100))
numbers_list = []
counter = 0

for n in numbers:
    numbers_list.append(n)
    random_number = random.choice(numbers_list)

while counter <= 5:

    for n in numbers_list:
        if user_guess == random_number:
            print("Correct!")
            exit()
        elif user_guess < random_number:
            user_guess = int(input("Your number is too small. Try again: "))
            counter += 1
            if counter == 5:
                print("Too many guesses.")
                print(random_number)
                print(counter+1)
                exit()
        elif user_guess > random_number:
            user_guess = int(input("Your number is too large. Try again: "))
            counter += 1
            if counter == 5:
                print("Too many guesses.")
                print(random_number)
                print(counter+1)
                exit()
else:
    exit()




