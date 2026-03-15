from board import Board

"""Represents a player with a name and symbol"""
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

""" It holds the board, players, and game loop"""
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "O"), Player("Player 2", "X")]
        self.current = 0

    """Returns whichever player should move next"""
    def current_player(self):
        return self.players[self.current]

    """asks the current player for input until a valid move is entered"""
    def get_move(self):
        while True:
            move = input(f"{self.current_player().name} ({self.current_player().symbol}), pick 0-8: ")
            """check if it is a valid digit and move is between 0 and 8 and square is empty"""
            if move.isdigit() and 0 <= int(move) <= 8 and self.board.is_valid(int(move)):
                return int(move)
            else:
                print("Invalid move, try again.")

    """it runs until someone wins or it's a tie"""
    def run(self):
        while True:
            """Print the current board """
            self.board.display()
            """Get a valid move from the current player and place their symbol on the board"""
            self.board.set(self.get_move(), self.current_player().symbol)


            """Check if the last move created a winning line"""
            if self.board.winner():
                """Show the board"""
                self.board.display()
                """Announce the winner by name"""
                print(f"{self.current_player().name} wins!")
                break
            """ check if the board is full"""
            if self.board.full():
                """Show the board"""
                self.board.display()
                print("It's a tie!")
                break

            """ switch players"""
            self.current = 1 - self.current