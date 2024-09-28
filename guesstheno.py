import random1 as guesstheno

ABC=guesstheno.game()
score=0
if  guesstheno.game.computer_choice==guesstheno.game.guess1:
    score=+1
else:
    print("your guess is wrong")