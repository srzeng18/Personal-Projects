print("Welcome to my adventure game!")
name = input("What is your name? ")
print("Hello", name + "!")
age = int(input("What is your age? "))

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
    else:
        print("Thanks for checking out my game. Have a good day!")
else:
    print("You are not old enough to play. Sorry!")
