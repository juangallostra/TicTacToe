import helper


class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """
    def __init__(self, dim, reverse=False, board=None):
        """
        Initialize the TTTBoard object with the given dimension and
        whether or not the game should be reversed.
        """
        self.dim = dim
        self.reverse = reverse
        # create board or use the one passed as argument
        if board is None:
            self.board = self.reset()
        else:
            self.board = board

        self.winning_combs = self.winning_combinations()

    def __str__(self):
        """
        Human readable representation of the board.
        """
        player_char = {helper.PLAYERX: 'X', helper.PLAYERO: 'O', helper.EMPTY: ' '}
        board_str = ''
        for row in range(self.dim):
            row_str = ' | '.join(player_char[self.board[row][i]] for i in range(self.dim))
            board_str += row_str
            if row != self.dim-1:  # Append a row separator to all but the last one
                board_str += '\n' + '-' * len(row_str) + '\n'
        return board_str

    def reset(self):
        """
        Create an empty board
        """
        return [[helper.EMPTY]*self.dim for dummy_row in range(self.dim)]

    def get_dim(self):
        """
        Return the dimension of the board.
        """
        return self.dim

    def square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO
        that correspond to the contents of the board at position (row, col).
        """
        return self.board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        return [(row, col) for row in range(self.dim) for col in range(self.dim) if self.board[row][col] == helper.EMPTY]

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        if player == helper.PLAYERO or player == helper.PLAYERX:
            if (row, col) in self.get_empty_squares():
                self.board[row][col] = player

    def winning_combinations(self):
        # Generate winning row and column combinations
        winning_combs = []
        for idx in range(self.dim):
            winning_row = tuple((idx, el) for el in range(self.dim))
            winning_col = tuple(coords[-1::-1] for coords in winning_row)
            winning_combs += [winning_row, winning_col]
        # Add diagonals
        # Up to down, left to right diagonal
        winning_combs += [tuple((el, el) for el in range(self.dim))]
        # Up to down, right to left diagonal
        winning_combs += [tuple(zip([el for el in range(self.dim)], [el for el in range(self.dim-1, -1, -1)]))]
        return winning_combs

    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """
        for winning_comb in self.winning_combs:
            plays_in_winning_comb = [self.square(row, col) for row, col in winning_comb]
            if all(player == plays_in_winning_comb[0] for player in plays_in_winning_comb):
                return plays_in_winning_comb[0]

        if not self.get_empty_squares():
            return helper.DRAW

        else:
            return None

    def clone(self):
        """
        Return a copy of the board.
        """
        return self.board

# TESTS
b = TTTBoard(3, False, [[2, 1, 1], [1, 2, 2], [2, 2, 1]])
print(str(b))
print(b.get_empty_squares())
# b.move(0,0,helper.PLAYERX)
print(str(b))
print(b.check_win())
