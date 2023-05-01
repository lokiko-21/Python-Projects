#
# Python: 3.11.1
#
# Author: Marco A. Breton
#
# Purpose: I will create a text game called nice or mean by
#          following along the instructor from The Tech Academy
#          and completing this small project.

def start(nice=0, mean=0, name=""):
    #get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
    check if this is a new game or not.
    if it is new, get the user's name.
    if it is not a new game, thank the player for
    playing again and continue with the game.
    """
    #meaning, if we do not already have this user's name
    #then they are a  new player and we need their name
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("What is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game you will interact \nwith several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger asks if you \nhave can spare some change \nand food for his family. \nWill you be nice \nor mean? (N/M) \n>>>").lower()
        if pick == "n":
            print("The stranger thanks you and \nwalks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("The stranger looks down in despair \nknowing his family won't eat...")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name) #PASS THE 3 VARIABLES TO THE score()


def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


#SHOWS CURRENT PLAYER'S SCORE
def score(nice, mean, name):
    #CALL WIN FUNCTION IF CONDITION IS MET
    if nice > 2:
        win(nice, mean, name)
    #CALL LOSE FUNCTION IF CONDITION IS MET
    if mean > 2:
        lose(nice, mean, name)
    #CALLS NICE/MEAN FUNCTION OTHERWISE
    else: nice_mean(nice, mean, name)


def win(nice, mean, name):
    #WIN CONDITION TEXT
    print("\nYour deeds are your monuments.\nGood things will come your way {}!".format(name))
    #CALL again() FUNCTION
    again(nice, mean, name)


def lose(nice, mean, name):
    print("\nA family has starved tonight {}.".format(name))
    again(nice, mean, name)


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice =="n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    #NOTICE NAME WAS NOT RESET AS THE SAME USER IS PLAYING AGAIN
    start(nice, mean, name)


if __name__ == "__main__":
    start()
