import random

print("Number Guessing Game")

# importing randint function to generate random number btwn 1 to 50
number = random.randint(1,50)

chances = 0
print("Guess a number (between 1 and 50): ")

# While loop to count the number of chances
while True:
	guess = int(input())

	if guess == number:
		print(f"Congratulations! You have guessed the Number {number} in {chances} attempts!")
		break
	# if number entered by user is same as generated number ny randint func
	# then break from loop

	elif guess < number:
		print(f"Your guess is lower. Guess number higher than {guess}")
	# Check if user guessed a number lower

	else:
		print(f"Your guess is higher. Guess number lower than {guess}")
	# Check if user guessed a number higher

	chances += 1
	# Incrementing the value of chances by 1
