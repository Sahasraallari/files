import random
def number_guessing_game():
    print("Welcome to the guessing game")
    seceret=random.randint(1,10)
    attempts=0
    while True:
        try:
            guess=int(input("Guss a number between 1 to 10:"))
            attempts +=1
            if guess< seceret:
                  print("Too low try again.")
            elif guess> seceret:
                  print("Too high try again.")
            else:
                  print("cangratulations you guesseg the number in {attempts} attempts")
                  break
        except ValueError:
          print("Please enter a valid number.")
if __name__ == "__main__":  
   number_guessing_game()
        

                  
                  