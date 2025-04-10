import random
def num_guess_game():
    print("welcome to guessing game")
    seceret=random.randint(1,10)
    attempts=0
    while True:
        try:
            guess=int(input("Guess a number between 1 to 10:"))
            attempts +=1
            if guess<seceret:
                print("Too low try again.")
            elif guess>seceret:
                print("Too high try again.")
            else:
                print("Congratulation you guess the number{attempts} attempts")
                break
        except ValueError:
            print("please enter a correct number")
if __name__ == "__main__":
   num_guess_game()




                
                

    
