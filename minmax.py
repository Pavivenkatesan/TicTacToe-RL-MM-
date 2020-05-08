import numpy as np
from math import inf as infinity

# Initializing the Tic-Tac-Toe environment
# Three rows-Three columns, creating an empty list of three empty lists
state_space = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
# No. of players = 2 : X & O
players = ['X','O']

# Defining the play state_value, player and the cell number
def play(sv, each_player, cell):
    if sv[int((cell-1)/3)][(cell-1)%3] is ' ':
        sv[int((cell-1)/3)][(cell-1)%3] = each_player
    else:
        cell = int(input(" Choose again, Cell is not empty: "))
        play(sv, each_player, cell)
    
# Defining new state function: which traverse over rows and columns and returns new state
def new(state):
    ns = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(3):
        for j in range(3):
            ns[i][j] = state[i][j]
    return ns
    
# Determining the current state value and determining the win
def cur_state(state_space):
  
    if (state_space[0][0] == state_space[0][1] and state_space[0][1] == state_space[0][2] and state_space[0][0] is not ' '):
        return state_space[0][0], "Done"
    if (state_space[1][0] == state_space[1][1] and state_space[1][1] == state_space[1][2] and state_space[1][0] is not ' '):
        return state_space[1][0], "Done"
    if (state_space[2][0] == state_space[2][1] and state_space[2][1] == state_space[2][2] and state_space[2][0] is not ' '):
        return state_space[2][0], "Done"
 
    if (state_space[0][0] == state_space[1][0] and state_space[1][0] == state_space[2][0] and state_space[0][0] is not ' '):
        return state_space[0][0], "Done"
    if (state_space[0][1] == state_space[1][1] and state_space[1][1] == state_space[2][1] and state_space[0][1] is not ' '):
        return state_space[0][1], "Done"
    if (state_space[0][2] == state_space[1][2] and state_space[1][2] == state_space[2][2] and state_space[0][2] is not ' '):
        return state_space[0][2], "Done"
    
    if (state_space[0][0] == state_space[1][1] and state_space[1][1] == state_space[2][2] and state_space[0][0] is not ' '):
        return state_space[1][1], "Done"
    if (state_space[2][0] == state_space[1][1] and state_space[1][1] == state_space[0][2] and state_space[2][0] is not ' '):
        return state_space[1][1], "Done"

  # if none of the above is true there must be a draw
    draw = 0
    for i in range(3):
        for j in range(3):
            if state_space[i][j] is ' ':
                draw = 1
    if draw is 0:
        return None, "Draw"
    
    return None, "Not Done"

# Defining the outline of the Tic-Tac Toe for the state_space or environment
def outline(state_space):
    print('----------------')
    print('| ' + str(state_space[0][0]) + ' || ' + str(state_space[0][1]) + ' || ' + str(state_space[0][2]) + ' |')
    print('----------------')
    print('| ' + str(state_space[1][0]) + ' || ' + str(state_space[1][1]) + ' || ' + str(state_space[1][2]) + ' |')
    print('----------------')
    print('| ' + str(state_space[2][0]) + ' || ' + str(state_space[2][1]) + ' || ' + str(state_space[2][2]) + ' |')
    print('----------------')
    
# Training our Tic-Tac-Toe agent on Minmax Algorithm
def MM(state, each_player):
    
    #Minimax Algorithm
    
    winner_loser , done = cur_state(state)
    if done == "Done" and winner_loser == 'O': # Agent win
        return 1
    elif done == "Done" and winner_loser == 'X': # Human win
        return -1
    elif done == "Draw":    # Draw 
        return 0
        
    moves = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] is ' ':
                empty_cells.append(i*3 + (j+1))
    
    for empty_cell in empty_cells:
        steps = {}
        steps['index'] = empty_cell
        new_state = new(state)
        play(new_state, each_player, empty_cell)
        
        if each_player == 'O':    
            result = MM(new_state, 'X')    
            steps['score'] = result
        else:
            result = MM(new_state, 'O')    
            steps['score'] = result
        
        moves.append(steps)

    # Finding the next best move
    best_move = None
    if each_player == 'O':   
        best = -infinity
        for steps in moves:
            if steps['score'] > best:
                best = steps['score']
                best_move = steps['index']
    else:
        best = infinity
        for steps in moves:
            if steps['score'] < best:
                best = steps['score']
                best_move = steps['index']
                
    return best_move


play_more = 'Y'
while play_more == 'Y' or play_more == 'y':
    state_space = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    curr_state = "Not Done"
    print("\n Let's start New Game!")
    outline(state_space)
    input_choice = input("Choose which player to go first - X (Human) or O(RL Agent): ")
    winner = None
    
    if input_choice == 'X' or input_choice == 'x':
        cid = 0
    else:
        cid = 1
        
    while curr_state == "Not Done":
        if cid == 0: 
            block_choice = int(input("It's your turn! Choose a block to place X (1 to 9):"))
            play(state_space ,players[cid], block_choice)
        else:   
            block_choice = MM(state_space, players[cid])
            play(state_space ,players[cid], block_choice)
            print("Agent O placed at " + str(block_choice))
        outline(state_space)
        winner, curr_state = cur_state(state_space)
        if winner is not None:
            print(str(winner) +  " Won Won Won!")
        else:
            cid = (cid + 1)%2
        
        if curr_state is "Draw":
            print("Draw Draw Draw!!!")
            
    play_more = input('Wanna Play more? Hit Y/N ')
    if play_more == 'N':
        print('See you again! :D')
    
