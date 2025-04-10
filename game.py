import random
def computer():
    return random. choice(['rock','paper,''scissors'])
def get_winner(player,computer):
    if player == computer:
        return "it's a tie"
    elif(player=='rock' and computer == 'sicssors')or\
     (player =='sicssors' and computer == 'paper')or\
     (player == 'paper' and computer == 'rock'):
        return "You win"
    else:
        return "Computer wins"
def main():
    while True:
        Player_choice=input("Enter rock,paper or scissors(or 'quit'to exit):").lower()
        if Player_choice == 'quit':
            print("Thanks for playing")
            break
        if Player_choice not in[ 'rock','paper','scissors']:
            print(" Invalid choice,try again.")
            continue
        computer_choice = computer()
        print(f"Computer choose:{computer_choice}")
        print(get_winner(Player_choice, computer_choice))
if __name__ == "__main__":
     main()


