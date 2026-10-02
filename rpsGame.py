#******Rude Rock Paper Scissors Game******

import random

print("***** Welcome to the Virtual Rock Paper Scissors Game *****\n")

#Define how to play and present user options.

print("The games relatively the same... you have to a choice of rock paper or scissors and then either your benefaction or doom awaits...\n")


user_score = 0

comp_score = 0

while True:
    user_action = input("Choose your weapon fool!! (Rock, Paper, Scissors): ").capitalize()

    poss_choices = ["Rock", "Paper", "Scissors"]

    if user_action == "q":
        break

    comp_action = random.choice(poss_choices)

    print("Computer chose:", comp_action)

    if user_action != "Rock" and user_action != "Paper" and user_action != "Scissors":
        print("Invalid Knave!! Choose Rock, Paper, or Scissors!\n")
    elif user_action == comp_action:
        print("Its a Tie... In other words, You LOSE CHARLATAN!!\n")
        print("My amazing score: ", comp_score, " Your Shame: \n", user_score)
    elif user_action == "Rock" and comp_action == "Paper":
        print("Hahahahahaha!!! What a failure you are!!! You LOSEEEEE!!\n")
        comp_score += 1
        print("My amazing score: ", comp_score, " Your Shame: \n", user_score)
    elif user_action == "Rock" and comp_action == "Scissors":
        print("I'll forfeit this time foolish human. Be wary, henceforth. Know I shall secede again. You win...\n")
        user_score += 1
        print("My amazing score: ", comp_score, " Your Shame: ", user_score)
    elif user_action == "Paper" and comp_action == "Scissors":
        print("How remedial can you be?!? You Fail!! Accept your demise!!\n")
        comp_score += 1
        print("My amazing score: ", comp_score, " Your Shame: ", user_score)
    elif user_action == "Paper" and comp_action == "Rock":
        print("You blind me and leave me defenseless... Maybe you aren't useless human. You win ig...\n")
        user_score += 1
        print("My amazing score: ", comp_score, " Your Shame: \n", user_score)
    elif user_action == "Scissors" and comp_action == "Rock":
        print("Wrong move human!! And now you shall pay the consequences!! You LOSEEEEEE, I WINNNNNNN!!\n")
        comp_score += 1
        print("My amazing score: ", comp_score, " Your Shame: ", user_score)
    elif user_action == "Scissors" and comp_action == "Paper":
        print("Foolish of me I suspect. Such a shame to be bested by a Human. Especially the likes of you. You win I suppose...\n")
        user_score += 1
        print("My amazing score: ", comp_score, " Your Shame: ", user_score)

    play_again = input("Do you want to play again? C'mon taste your shame again fleshbucket!! (y/n): \n")

    if play_again == "n":
        break