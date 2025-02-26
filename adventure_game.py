print("Welcome to my adventure game!")
name = input("What is your name? ")
print("Hello", name + "!")
age = int(input("What is your age? "))

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play (yes/no)? ").lower()
    if wants_to_play == "yes":
        health = 10
        print("You are starting with", health, "health.")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow a path and reach a lake... Do you swim across or go around (swim/around)? ").lower()

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "swim":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5
                print("Health count: ", health)
            
            ans = input("You continue along the path and reached a house. Do you knock or pass by it (knock/pass)? ").lower()
            
            if ans == "knock":
                print("The door creaked open...")

                ans = input("An old lady appeared and offers you tea. Do you take her offer (yes/no)? ").lower()
                if ans == "yes":
                    print("Congrats! You earned 3 health.")
                    health += 3
                    print("Health count: ", health)
                    print("You continue the journey.")
                else:
                    print("You had a nice conversation with the lady and she gave you encouragement on your journey. You continue the path.")
            else:
                print("You admired the house and went about your journey.")
            
            ans = input("You then stumble upon a forest of mushrooms. By this time, you are starving and only have a piece of bread. Do you eat the mushrooms (yes/no)? ").lower()

            if ans == "yes":
                print("Oh no! Some mushrooms had some mold and you got a bad stomach bug. You lost 5 health.")
                health -= 5
                print("Health count: ", health)
                if health <= 0:
                    print("You have no more health. You lost!")
                else:
                    print("You managed to get far enough to find shelter. Congrats! You have survived the day. Thanks for playing my game.")
            else:
                print("You ate the one piece of bread you had and managed to get far enough to find shelter. Congrats! You have survived the day. Thanks for playing my game.")

        else:
            print("Better luck next time. You lost!")

    else:
        print("Thanks for checking out my game. Have a good day!")
else:
    print("You are not old enough to play. Sorry!")
