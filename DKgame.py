import random
import time

def display_intro():
    print("You are in the Kingdom of Dragons. In front of you, you see two caves. "
            "In one cave, the dragon is friendly and will share his treasure with you. "
          "The other dragon is hungry and will eat you on sight.")
    time.sleep(4)

def choose_cave():
    cave_number=int(input("Want to enter cave 1 or 2? : "))
    if cave_number==random.randint(1,2):
        print("Friendly Dragon. Share his treasure with you.")
        print("You won.")
    else:
        print("Hungry Dragon. Eat you on sight.")
        print("You lose.")
        print("\n")
    again=input("Do you want to play again? Yes-y or No-n : ")
    if again=="y":
        display_intro()
        choose_cave()
    else:
        print("Finish.")

display_intro()
choose_cave()




