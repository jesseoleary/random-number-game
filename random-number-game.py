import random

number = random.randint(0,100)
counter = int()
guess = int()

while guess != number:
    guess = int(input('guess random number: '))
    counter += 1
    if guess > number:
        print('lower')
    if guess < number:
        print('higher')

print('yes! the number was {0}. you guessed correct! It took you {1} guesses.'
      .format(number, counter))
