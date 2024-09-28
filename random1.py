import random
class game:
    def computer_choice():
        computer_choose=random.randint(1,100)
        return computer_choose 
    def guess1():
        guess=input("gues aa number: ")
        if guess.isdigit():
            print("let the compter choose:")
        else:
            guess=int(guess)
x=game.guess1()
print(game.computer_choice())