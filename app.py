# the grid made for the tic-tac-toe
grid = [["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

# All the winning combinations that could be like having like the winning combination
winning_combination = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    # Diagonal
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


def check_win(ltr):
    for combo in winning_combination:
        if all(grid[row][column] == ltr for row, column in combo):
            return True
    return False


def check_tie():
    for row in grid:
        for cell in row:
            if cell in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False

    return True


# function to print the grid for the tic-tac-toe
def print_grid():
    print(grid[0])
    print("...............")
    print(grid[1])
    print("...............")
    print(grid[2])


def reset_grid():
    return [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]



#
def put_letter(ltr, pos):
    positions = {
        "1": (0,0),
        "2": (0,1),
        "3": (0,2),
        "4": (1,0),
        "5": (1,1),
        "6": (1,2),
        "7": (2,0),
        "8": (2,1),
        "9": (2,2)
    }
    if pos not in positions:
        return False

    row, column = positions[pos]

    if grid[row][column] != pos:
        return False

    grid[row][column] = ltr
    return True




# the main function for like tic-tac-toe
# this is going to have like the whole tic-tac-toe in it
def tic_tac_toe():
    Notwin = True
    while Notwin:
        print_grid()
        Xpos = input("choose where to put X:")
        if not put_letter("X", Xpos):
            print_grid()
            print("please choose correct value")
            Xpos2 = input("choose where to put X:")
            put_letter("X", Xpos2)
        if check_win("X"):
            print("X wins")
            break
        if check_tie():
            print("it is a TIEEE!!!")
            break
        print_grid()
        Opos = input("choose where to put O:")
        if not put_letter("O", Opos):
            print_grid()
            print("please choose correct value")
            Opos2 = input("choose where to put O:")
            put_letter("O", Opos2)
        if check_win("O"):
            print("O wins")
            break
        if check_tie():
            print("it is a TIEEE!!!")
            break


match_style = input("enter the numeric values \n"
                    "1: Single\n"
                    "2: Tournument\n"
                    "Enter:")

if match_style == "1":
    tic_tac_toe()
if match_style == "2":
    matchesnum = int(input("Enter the number of maches you want to play:"))
    Xpoints = 0
    Opoints = 0
    ties = 0
    for i in range(matchesnum):
        tic_tac_toe()
        if check_win("X"):
            Xpoints += 1
        elif check_win("O"):
            Opoints += 1
        elif check_tie():
            ties += 1

        print("| Players | Points |")
        print(f"|   X     | {Xpoints} |")
        print(f"|   O     | {Opoints} |")
        print(f"| Tie     | {ties} |")

        grid = reset_grid()

    if Xpoints > Opoints:
        print("x wins")
    if Opoints > Xpoints:
        print("O wins")
    if Xpoints == Opoints:
        print("its a draw")
