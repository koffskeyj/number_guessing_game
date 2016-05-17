import random

user_input = int(input("Please enter a number for the computer: "))
numbers = (range(100))
numbers_list = []
counter = 0

for n in numbers:
    numbers_list.append(n)

while counter <= 5:

    for n in numbers_list:
        computer_number = random.choice(numbers_list)
        print(computer_number)
        if computer_number == user_input:
            print("Computer is correct!")
            exit()
        elif computer_number < user_input:
            print("The computer guessed a smaller number. It will try again: ")
            counter += 1
            if counter == 5:
                print("Too many guesses.")
                print(counter)
                exit()
        elif computer_number > user_input:
            print("The computer guessed a larger number. It will try again: ")
            counter += 1
            if counter == 5:
                print("Too many guesses.")
                print(counter)
                exit()
else:
    print("The computer wins!")