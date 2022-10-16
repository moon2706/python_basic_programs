import random
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
    print("Rolling the Dice\n"
          "The values are...")
    print(random.randint(1,6))    # min value= 1
    print(random.randint(1,6))    # max value= 6
    roll_again=input("Roll Dice again?")