class OxoBoard:
    def __init__(self):
        self.gameboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Initialises the gameboard list

    def get_square(self, x, y):
        return self.gameboard[x][y] #Returns the value of a square on the gameboard

    def set_square(self, x, y, mark):
        if self.gameboard[x][y] == 0:  #Checks if a square is empty, if so it's filled with mark, if not False is returned
            self.gameboard[x][y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        for x in range(3):  #Returns a false boolean if any squares on the board are empty
            for y in range(3):
                if self.gameboard[x][y] == 0:
                    return False
        return True


    def get_winner(self):
        for i in range(3):
            # Checks for Vertical matches, >0 checks that none of the squares are empty
            if self.gameboard[0][i] == self.gameboard[1][i] == self.gameboard[2][i] > 0:
                return current_player
            # Checks for Horizontal matches
            elif self.gameboard[i][0] == self.gameboard[i][1] == self.gameboard == [i][2] > 0:
                return current_player
            # Checks for Diagonal matches
            elif self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[0][0] > 0:
                return current_player
            elif self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2] > 0:
                return current_player
        return 0


    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in range(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard()
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                print "Player", winner, "wins!"
                break   # End the game
            elif board.is_board_full():
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
