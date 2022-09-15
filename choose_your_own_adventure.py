name = input("Hi traveller. What is your name? ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end, and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    print()
    answer = input(
        "You come to a river, and you can walk around it or swim accross. Type walk or swim: ")
    if answer == "walk":
        print("You walked for many miles and were eaten by a bear. ")
    elif answer == "swim":
        print("You swam acrross and were eaten by an alligator. ")
    else:
        print("Not a valid option. Meh. ")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly. Do you want to cross or go back? ")
    if answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to him (Yes/No()?: ) ")
        if answer == "yes":
            print("You talk to the stranger and he gives you a coin of gold. Siuu!. ")
        elif answer == "no":
            print("The stranger eats you. ")
        else:
            print("Not a valid option. Meh. ")
    elif answer == "go back":
        print("You go back were eaten by a snake. ")
    else:
        print("Not a valid option. Meh. ")

else:
    print("Not a valid option. Meh. ")

print("Thanks for playing", name, ". The force may be with you.")