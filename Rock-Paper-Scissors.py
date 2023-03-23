import random

class Player():
    def point(self):
        self.score += 1

class HumanPlayer(Player):
    def __init__(self):
        self.score = 0
        self.choice = ''

    def get_choice(self):
        ch = ''
        while ch not in ['r', 'p', 's']:
            try:
                ch = input("Rock, paper, or scissors [r/p/s]? ").lower()
            except:
                print("Please enter a valid input!")
            else:
                if ch not in ['r', 'p', 's']:
                    print("Please enter a valid input!")
                else:
                    self.choice = ch
                    return ch

class ComputerPlayer(Player):
    def __init__(self):
        self.score = 0
        self.choice = ''

    def get_choice(self):
        self.choice = random.choice('rps')
        return self.choice


class Game():

    def __init__(self):
        self.num_rounds = 0
        print("\n--- Rock Paper Scissors Game ---")
        pass

    def rounds(self):
        num_rounds = -1
        while True:
            try:
                num_rounds = int(input("How many rounds would you like to play?"))
            except:
                print("Please enter a number!")
            else:
                if num_rounds < 1:
                    print("Rounds cannot be under 1, please enter again!")
                else:
                    break

        return num_rounds

def main():
    new_game = Game()
    num_rounds = new_game.rounds()
    new_player = HumanPlayer()
    new_computer = ComputerPlayer()
    counter = 0
    while counter < num_rounds:
        new_player.get_choice()
        new_computer.get_choice()
        comb = new_player.choice + new_computer.choice
        print(f"You: {new_player.choice}   |  Computer: {new_computer.choice}")
        if new_player.choice == new_computer.choice:
            print("Round is tied!")
            counter += 1
        elif comb in ['rp', 'ps', 'sr']:
            print("You lost this round!")
            counter += 1
            new_computer.point()
        else:
            print("You won this round!")
            counter += 1
            new_player.point()

    print(f"[Game summary] Your points: {new_player.score}   |  Computer points: {new_computer.score}")
    if new_player.score == new_computer.score:
        print("Tied Game!")
    elif new_player.score > new_computer.score:
        print("You won!")
    else:
        print("You lost!")

if __name__ == '__main__':
    main()