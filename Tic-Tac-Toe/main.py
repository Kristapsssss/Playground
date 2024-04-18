game = True

while game:
    Round = True
    print("Welcome to Tic Tac Toe\n")

    # A dictionary to hold the value of board grids: blank, X or O.
    game_dictionary = {'A': {'1': ' ', '2': ' ', '3': ' '},
                       'B': {'1': ' ', '2': ' ', '3': ' '},
                       'C': {'1': ' ', '2': ' ', '3': ' '}}

    # Print Board to Console
    def board():
        return print(f"    A   B   C \n"
                     f"1  !{game_dictionary['A']['1']}! !{game_dictionary['B']['1']}! !{game_dictionary['C']['1']}!\n"
                     f"2  !{game_dictionary['A']['2']}! !{game_dictionary['B']['2']}! !{game_dictionary['C']['2']}!\n"
                     f"3  !{game_dictionary['A']['3']}! !{game_dictionary['B']['3']}! !{game_dictionary['C']['3']}!\n")


    x_turn = True

    print("X starts, choose an empty grid and try to make an uninterrupted line of 3.")
    board()

    while Round:
        choice = input("Choose a grid (example: A1): ")
        # Validate Input
        if len(choice) != 2 or choice[0] not in ['A', 'B', 'C'] or choice[1] not in ['1', '2', '3']:
            print("Please choose a valid input.")
            continue
        # Set first input letter as the column (A, B or C), second number character as the row (1, 2 or 3)
        col, row = choice[0], choice[1]

        # Check if Grid is Occupied
        if game_dictionary[col][row] != ' ':
            print("Grid has already been taken, try another one.")
            continue

        if x_turn:
            game_dictionary[col][row] = 'X'
        else:
            game_dictionary[col][row] = 'O'

        # Check for Winner in Columns
        for column in ['A', 'B', 'C']:
            if list(game_dictionary[column].values()) == ['X', 'X', 'X'] or \
                    list(game_dictionary[column].values()) == ['O', 'O', 'O']:
                board()
                print("\nPlayer Wins!\n")

                # Prompt for replay and prompt validation

                play_again = input("Would you like to play again? (yes/no): ")
                while play_again != 'yes' and play_again != 'no':
                    play_again = input("Try again.. (yes/no): ")
                if play_again == 'yes':
                    Round = False
                else:
                    Round = False
                    game = False
                break

        # Check for Winner in Rows
        for row in ['1', '2', '3']:
            if game_dictionary['A'][row] == game_dictionary['B'][row] == game_dictionary['C'][row] != ' ':
                board()
                print("\nPlayer Wins!\n")

                # Prompt for replay and prompt validation

                play_again = input("Would you like to play again? (yes/no")
                while play_again != 'yes' and play_again != 'no':
                    play_again = input("Try again.. (yes/no): ")
                if play_again == 'yes':
                    Round = False
                else:
                    Round = False
                    game = False
                break

        # Check for Winner Diagonally
        if game_dictionary['A']['1'] == game_dictionary['B']['2'] == game_dictionary['C']['3'] != ' ' or \
                game_dictionary['A']['3'] == game_dictionary['B']['2'] == game_dictionary['C']['1'] != " ":
            board()
            print("\nPlayer Wins!\n")

            # Prompt for replay and prompt validation

            play_again = input("Would you like to play again? (yes/no")
            while play_again != 'yes' and play_again != 'no':
                play_again = input("Try again.. (yes/no): ")
            if play_again == 'yes':
                Round = False
            else:
                Round = False
                game = False
            break

        # Check for Draw
        if all(value != ' ' for row in game_dictionary.values() for value in row.values()):
            board()
            print("\nIts a Draw!\n")

            # Prompt for replay and prompt validation

            play_again = input("Would you like to play again? (yes/no")
            while play_again != 'yes' and play_again != 'no':
                play_again = input("Try again.. (yes/no): ")
            if play_again == 'yes':
                Round = False
            else:
                game = False
                Round = False
            break

        # Switch Turns
        x_turn = not x_turn

        board()
