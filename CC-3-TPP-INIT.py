import random

secret_number = random.randint(1, 10)
attempts = 3

print("Guess the number (1 to 10)")
print("You have 3 attempts")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 You win!")
        break
    else:
        attempts -= 1
        print("Wrong guess!")

if attempts == 0:
    print("Game over!")
    print("The number was:", secret_number)
