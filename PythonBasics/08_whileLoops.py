# Numbers 1-100, multiple of 3 = Fizz, multiple of 5 = "Buzz", multipe of 3 and 5 v = "FizzBuzz"

x = 1

while x < 101:

    if x % (3*5) == 0:
        print(x, "FizzBuzz")
    elif x % 3 == 0:
        print(x, "Fizz")
    elif x % 5 == 0:
        print(x, "Buzz")
    else:
        print(x)

    x = x + 1



# build a guessing game. The number to be guessed is "9".  You have 3 guesses to make until you loose
guessCount = 1
number = 9

while guessCount<=3:
    guessing = int(input("Guess: "))
    if guessing == number:
        print("You win! :)")
        break
    elif guessing != number:
        guessCount = guessCount + 1  # oder guessCount += 1
else: print("Sorry you failed! :c")

