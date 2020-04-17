import random

SIZE = 7
def create_board():
    board = []
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            row.append('-')
        board.append(row)
    g_pos = random.randint(0, SIZE-1)
    board[0][g_pos] = 'G'
    board[1] = ['P'] * SIZE
    indexes = list(range(SIZE))
    random.shuffle(indexes)
    board[-1][indexes[0]] = 'B'
    board[-1][indexes[1]] = 'B'
    board[-1][indexes[2]] = 'R'
    board[-1][indexes[3]] = 'R'
    return board

def set_traps():
    trap_map = []
    for i in range(1, SIZE-1):
        for j in range(SIZE):
            if random.random() < 0.2:
                trap_map.append([i, j])
    print("{} traps".format(len(trap_map)))
    return trap_map

def display_board(board):
    string1 = "  "
    string2 = " +"
    for i in range(SIZE):
        string1 += str(i)
        string2 += '='
    string2 += '+'
    print(string1)
    print(string2)
    for i in range(SIZE):
        string = str(i) + '|'
        for j in range(SIZE):
            string += board[i][j]
        string += '|' + str(i)
        print(string)
    print(string2)
    print(string1)

def validate_moves(row_i, column_i, row_o, column_o, board):
    pass

def check_traps(row_i, column_i, row_o, column_o, trap_map):
    pass

def move_general(board):
    pass

def move_soldier(row_i, column_i, row_o, column_o, board, trap_map):
    pass

def main():
    board = create_board()
    trap_map = set_traps()
    display_board(board)

main()
