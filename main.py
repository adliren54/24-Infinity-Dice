import random
print("Infinity Dice 🎲")

def dice(sides):
  while True:
    result = random.randint(1, sides)
    print("You rolled", result)
    proceed = input("Roll again? ")
    if proceed == "yes":
      continue
    elif proceed == "no":
      break
    else:
      print("What??")
      exit()

userSides = int(input("How many sides?: "))
dice(userSides)