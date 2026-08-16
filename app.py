grid = [["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

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


def print_grid():
    print(grid[0])
    print("...............")
    print(grid[1])
    print("...............")
    print(grid[2])


def reset_grid():
    grid = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]
    return grid


def put_letter(ltr, pos):
    if pos == "1" and grid[0][0] == "1":
        grid[0][0] = ltr
    if pos == "2" and grid[0][1] == "2":
        grid[0][1] = ltr
    if pos == "3" and grid[0][2] == "3":
        grid[0][2] = ltr
    if pos == "4" and grid[1][0] == "4":
        grid[1][0] = ltr
    if pos == "5" and grid[1][1] == "5":
        grid[1][1] = ltr
    if pos == "6" and grid[1][2] == "6":
        grid[1][2] = ltr
    if pos == "7" and grid[2][0] == "7":
        grid[2][0] = ltr
    if pos == "8" and grid[2][1] == "8":
        grid[2][1] = ltr
    if pos == "9" and grid[2][2] == "9":
        grid[2][2] = ltr


def tic_tac_toe():
    Notwin = True
    while Notwin:
        print_grid()
        Xpos = input("choose where to put X:")
        put_letter("X", Xpos)

        if check_win("X"):
            print("X wins")
            break
        if check_tie():
            print("it is a TIEEE!!!")
            break
        print_grid()
        Opos = input("choose where to put O:")
        put_letter("O", Opos)
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
