import random

class RockPaperScissors:
    def __init__(self):
        self.comp_wins = 0
        self.player_wins = 0
    
    @staticmethod    
    def instructions():
       text =  '''
        To play, you need type:
        rock
        paper
        scissors
        '''
       return text
        
    def game_proccess(self):
        comp_step = random.choice(['rock','paper','scissors'])
        players_step = input('Input your step: ')
        if comp_step == players_step:
            print(f'Both choose {players_step},try again')
            return self.game_proccess()
        
        elif players_step == 'rock':
            if comp_step == 'sccisors':
                print('Player wins')
                self.player_wins += 1
            elif comp_step == 'paper':
                print('Computer wins')
                self.comp_wins += 1
        
        elif players_step == 'paper':
            if comp_step == 'sccisors':
                print('Computer wins')
                self.comp_wins += 1
            elif comp_step == 'rock':
                print('Player wins')
                self.player_wins += 1
        
        elif players_step == 'sccisors':
            if comp_step == 'rock':
                print('Computer wins')
                self.comp_wins += 1
            elif comp_step == 'paper':
                print('Player wins')
                self.player_wins += 1
        
        else:
            print('Invalid move,try again')
            return self.game_proccess()
                    
def main():
    game = RockPaperScissors()
    print('''Welcome to Rock Paper Scissors game!
          Instructions - I
          Game - G
          Exit - Any key''')
    _ = input('Choose: ')
    if _ == 'I':
        game.instructions()
        return main()
    elif _ == 'G':
        sets = int(input('How many sets you want to play?'))
        while sets:
            game.game_proccess()
            print(f'Player score: {game.player_wins}, computer score: {game.comp_wins}')
            sets -= 1
        return main()
    else:
        print('Thank you!')
        exit()
        
main()