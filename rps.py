import random

while True:
    def play():

        user = input("Enter r for rock, s for scissors, p for paper: ").lower()

        computer_choice = random.choice(r, s, p)

        if user == computer_choice:
            return 'It\'s a Tie'

        if is_win():
            print('You have won!')
            
        return 'You lost'



    def is_win():
        if (user == p and computer_choice == r) or (user == s and computer_choice == p) or (user == r and computer_choice == s):
            return True
        


print(play())
