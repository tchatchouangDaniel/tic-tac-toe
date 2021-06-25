import random

def trace_board(listItems) : 
    """trace the gameboard for the tic tac toe with
    the corresponding symbols in the corresponding 
    tyles.

    Args:
        listItems (list(string)): a list that keep the 
        different symbols with the index as position
    """
    board = "| {0} | {1} | {2} |\n-------------\n| {3} | {4} | {5} |\n-------------\n| {6} | {7} | {8} |"
    board = board.format(*listItems)
    print(board)

def play(current_player, gameboard) :
    """used to make players play on the board

    Args:
        current_player (string): the current player symbols
        gameboard (list(string)): a list containing the different 
        position of the game with the symbol

    Raises:
        ValueError: raise an error when the position selected is not available
        ValueError: raise an error when the position selected is out of bounds
    """
    print('player {} Turn :\n'.format(current_player))
    position = -1
    while True :
        try :
            position = int(input("Enter position : "))
            if position < 1 and position > 9 : 
                raise ValueError('The position entered is not on board')
            if gameboard[position-1]  == 'O' or gameboard[position-1] == 'X' :
                raise ValueError('The position is occupied')
            break
        except KeyboardInterrupt :
            print('\n\nNo input provided\nGAME OVER!!!')
            break
        except Exception as e:
            print('not valid input try again ^^ : {}\n'.format(e))
    if position != -1 :
        gameboard[position-1] = current_player
        trace_board(gameboard)

def welcome(gameboard) : 
    """A function that generates the gameboard and randomly
    select the first player

    Args:
        gameboard (list(string)): the list containing informations about the gameboard

    Returns:
        string: the player that begin
    """
    print('WELCOME TO DANIEL\'S TIC-TAC-TOE')
    trace_board(gameboard)
    return random.choice(['O','X'])

def check_end_game(gameboard,current_player) : 
    winning_positions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,4,8],
        [6,4,2],
        [0,3,6],
        [1,4,7],
        [2,5,8]
    ]
    for position in winning_positions :
        if gameboard[position[0]] == current_player and gameboard[position[1]] == current_player and gameboard[position[2]] == current_player :
            print("Player {} Win".format(current_player))
            return True
    return False

def game_sequence():
    """support the game logic to play a complete game between two players
    """
    stop = False
    gameboard = ['1','2','3','4','5','6','7','8','9']
    current_player = welcome(gameboard)
    while not stop :
        play(current_player,gameboard)
        stop = check_end_game(gameboard,current_player)
        current_player = 'O' if current_player == 'X' else 'X'

def main() :
    game_sequence()
    
if __name__ == '__main__' :
    main()