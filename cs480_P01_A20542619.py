import math, sys

class TicTacToe:
    
    # check if game is over
    @staticmethod
    def isTerminal(state):
        endStates = [[0,1,2],[3,4,5],[6,7,8],
                     [0,3,6],[1,4,7],[2,5,8],
                     [0,4,8],[2,4,6]]
        for i in endStates:
            if (state[i[0]] == state[i[1]] == state[i[2]]) and (state[i[2]] != " "):
                return True, state[i[2]] 
        if " " not in state:
            return True, 0
        return False, None
    
    # return whose move it is (defaulted to "x" going first)
    @staticmethod
    def toMove(state, first):
        ret = ""
        countX = 0
        countO = 0
        for i in state:
            if i == "x":
                countX += 1
            if i == "o":
                countO += 1
        if countX == countO:
            if first == "x":
                ret = "x"
            else:
                ret = "o"
        else:
            if first == "x":
                ret = "o"
            else:
                ret = "x"
        return ret
        
    # return -1 0 1 for loss win draw for specified player
    @staticmethod
    def utility(state, player):
        result = TicTacToe.isTerminal(state)[1]
        if result == None:
            raise TypeError
        if result == 0:
            return 0
        elif result == player:
            return 1
        else:
            return -1
    
    # return all possible moves
    @staticmethod
    def actions(state):
        lst = []
        for i in range(len(state)):
            if state[i] == " ":
                lst.append(i)
        lst.sort()
        return lst
    
    #return state after action "a"
    @staticmethod
    def result(state, a, first):
        ret = state.copy()
        val = TicTacToe.toMove(state, first)
        ret[a] = val
        return ret
    
    #print board grid
    @staticmethod
    def printGrid(state):
        string = " {} | {} | {} \n---+---+---\n {} | {} | {} \n---+---+---\n {} | {} | {} \n".format(state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8])
        print(string)

# minmax no pruning

node_number = 0

def minimax_search(game, state, player, first):

    def max_value(game, state):
        if game.isTerminal(state)[0]:
            global node_number
            node_number += 1
            return game.utility(state, player), None
        v = -math.inf
        for a in game.actions(state):
            v2, a2 = min_value(game, game.result(state, a, first))
            if v2 > v:
                v, move = v2, a
        return v, move

    def min_value(game, state):
        if game.isTerminal(state)[0]:
            global node_number
            node_number += 1
            return game.utility(state, player), None
        v = math.inf
        for a in game.actions(state):
            v2, a2 = max_value(game, game.result(state, a, first))
            if v2 < v:
                v, move = v2, a
        return v, move

    global node_number
    node_number = 0

    value, move = max_value(game, state)

    ret = node_number
    node_number = 0

    return move, value, ret

# minmax with pruning

node_number_pruned = 0

def alpha_beta_search(game, state, player, first):

    def max_value_pruned(game, state, alpha, beta):
        if game.isTerminal(state)[0]:
            global node_number_pruned
            node_number_pruned += 1
            return game.utility(state, player), None
        v = -math.inf
        for a in game.actions(state):
            v2, a2 = min_value_pruned(game, game.result(state, a, first), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    def min_value_pruned(game, state, alpha, beta):
        if game.isTerminal(state)[0]:
            global node_number_pruned
            node_number_pruned += 1
            return game.utility(state, player), None
        v = math.inf
        for a in game.actions(state):
            v2, a2 = max_value_pruned(game, game.result(state, a, first), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move
    
    
    global node_number_pruned
    node_number_pruned = 0
    
    value, move = max_value_pruned(game, state, -math.inf, math.inf)

    ret = node_number_pruned
    node_number_pruned = 0

    return move, value, ret

def flip(val):

    if val == "x":
        return "o"
    else:
        return "x"

#play the game

# board = [" "," "," ",
#          " "," "," ",
#          " "," "," "]
# print(TicTacToe.toMove(board, "o"))

def play(ALGO, FIRST, MODE):
    print("Shuaipaj, Besnik, A20542619 solution:")
    if ALGO == "1":
        print("Algorithm: MiniMax")
    else:
        print("Algorithm: MiniMax with alpha-beta pruning")

    print("First: "+FIRST.upper())

    if MODE == "1":
        print("Mode: human (X) versus computer (O)")
    else:
        print("Mode: computer (X) versus computer (O)")
    
    foo = [None,minimax_search,alpha_beta_search]

    if MODE == "1":
        board = [" "," "," ",
                 " "," "," ",
                 " "," "," "]
        
        while not TicTacToe.isTerminal(board)[0]:
            if TicTacToe.toMove(board, FIRST.lower()) == "x":
                move = input("X’s move. What is your move (possible moves at the moment are: "+ str(tuple([x+1 for x in TicTacToe.actions(board)])) +" | enter 0 to exit the game)?\n")
                while int(move) not in [x+1 for x in TicTacToe.actions(board)]:
                    if move == "0":
                        exit()
                    move = input("X’s move. What is your move (possible moves at the moment are: "+ str(tuple([x+1 for x in TicTacToe.actions(board)])) +" | enter 0 to exit the game)?\n")
                board = TicTacToe.result(board, int(move)-1, FIRST)
            else:
                search = foo[int(ALGO)](TicTacToe, board, player= "o", first = FIRST)
                move = search[0]
                nodes = search[2]
                print("O’s selected move: "+str(move+1)+". Number of search tree nodes generated: "+str(nodes)+ "\n")
                board = TicTacToe.result(board, move, FIRST)
                TicTacToe.printGrid(board)
        state = TicTacToe.isTerminal(board)[1]
        if state == 0:
            print("TIE")
        else:
            print(state.upper()+ " WON")
                

    else:
        board = [" "," "," ",
                 " "," "," ",
                 " "," "," "]
        
        while not TicTacToe.isTerminal(board)[0]:
            if TicTacToe.toMove(board, FIRST.lower()) == "x":
                search = foo[int(ALGO)](TicTacToe, board, player= "x", first = FIRST)
                move = search[0]
                nodes = search[2]
                print("X’s selected move: "+str(move+1)+". Number of search tree nodes generated: "+str(nodes)+ "\n")
                board = TicTacToe.result(board, move, FIRST)
                TicTacToe.printGrid(board)

            else:
                search = foo[int(ALGO)](TicTacToe, board, player= "o", first = FIRST)
                move = search[0]
                nodes = search[2]
                print("O’s selected move: "+str(move+1)+". Number of search tree nodes generated: "+str(nodes)+ "\n")
                board = TicTacToe.result(board, move, FIRST)
                TicTacToe.printGrid(board)
        state = TicTacToe.isTerminal(board)[1]
        if state == 0:
            print("TIE")
        else:
            print(state.upper()+ " WON")
        pass


if len(sys.argv) != 4:
    print("ERROR: Not enough/too many/illegal input arguments")
    exit()

# 	ALGO specifies which algorithm the computer player will use:
# 	1 – MiniMax,
# 	2 – MiniMax with alpha-beta pruning,
# 	FIRST specifies who begins the game:
# 	X
# 	O
# 	MODE is mode in which your program should operate:
# 	1 – human (X) versus computer (O),
# 	2 – computer (X) versus computer (O),

ALGO = sys.argv[1] 
FIRST = sys.argv[2].lower()
MODE = sys.argv[3]

play(ALGO,FIRST,MODE)