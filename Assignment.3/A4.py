import random
target = random.randint(1, 100)
while True:
    guess = int(input("Guess the number (from 1 to 100): "))
    if guess < 0:
      print("End program")
      break
    if guess > target:
     print("Too high")
    elif guess < target:
     print("Too low")
    else:
      print("Correct")
      break


                