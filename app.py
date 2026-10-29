# MAIN TIC-TAC-TOE GRID
grid = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# WINNING COMBINATIONS

winning_combination = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


# The main function to CHECK WIN
def check_win(ltr):
    for combo in winning_combination:
        if all(grid[row][column] == ltr for row, column in combo):
            return True

    return False


# The main function to CHECK TIE
def check_tie():
    for row in grid:
        for cell in row:
            if cell not in ("X", "O"):
                return False
    return not check_win("X") and not check_win("O")


# The function to PRINT GRID
def print_grid():
    print(grid[0])
    print("...............")
    print(grid[1])
    print("...............")
    print(grid[2])


# The function to RESET GRID

def reset_grid():
    return [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]


# The function to PUT X or O in this game

def put_letter(ltr, pos):
    positions = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "9": (2, 2)
    }

    if pos not in positions:
        return False

    row, column = positions[pos]

    if grid[row][column] != pos:
        return False

    grid[row][column] = ltr

    return True


# SINGLE MATCH

def tic_tac_toe():
    while True:

        print_grid()

        while True:
            Xpos = input("Choose where to put X: ")

            if put_letter("X", Xpos):
                break

            print("Please choose a valid and empty position.")

        if check_win("X"):
            print_grid()
            print("X wins!")
            return "X"

        if check_tie():
            print_grid()
            print("It is a TIEEE!!!")
            return "tie"

        print_grid()

        while True:
            Opos = input("Choose where to put O: ")

            if put_letter("O", Opos):
                break

            print("Please choose a valid and empty position.")

        if check_win("O"):
            print_grid()
            print("O wins!")
            return "O"

        if check_tie():
            print_grid()
            print("It is a TIEEE!!!")
            return "tie"


# GAME MODE

match_style = input(
    "Enter the numeric value:\n"
    "1: Single\n"
    "2: Tournament\n"
    "Enter: "
)

# SINGLE MODE

if match_style == "1":

    tic_tac_toe()


# TOURNAMENT MODE

elif match_style == "2":

    while True:
        try:
            matchesnum = int(input("How many matches do you want to play? "))
            if matchesnum > 0:
                break
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")

    Xpoints = 0
    Opoints = 0
    ties = 0

    for i in range(matchesnum):

        print(f"\n========== MATCH {i + 1} ==========\n")

        result = tic_tac_toe()

        # Store the result
        if result == "X":
            Xpoints += 1

        elif result == "O":
            Opoints += 1

        elif result == "tie":
            ties += 1

        # Display current score
        print("\n| Players | Points |")
        print(f"| X       | {Xpoints}      |")
        print(f"| O       | {Opoints}      |")
        print(f"| Ties    | {ties}      |")

        # Resetting  the board for the next match
        grid = reset_grid()

    # TOURNAMENT WINNER

    print("\n TOURNAMENT RESULT ")

    if Xpoints > Opoints:
        print("X wins the tournament!")

    elif Opoints > Xpoints:
        print("O wins the tournament!")

    else:
        print("The tournament is a draw!")