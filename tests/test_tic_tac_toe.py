import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from board import Board
from game import Game

"""Tests for the Board class"""
class TestBoard(unittest.TestCase):

    """Create a fresh board before each test."""
    def setUp(self):
        self.board = Board()

    """A new board should have no winner"""
    def test_empty_board_has_no_winner(self):
        self.assertIsNone(self.board.winner())

    """A new board should not be full"""
    def test_empty_board_is_not_full(self):
        self.assertFalse(self.board.full())

    """X should win when the top row is filled"""
    def test_row_win(self):
        for i in [0, 1, 2]:
            self.board.set(i, "X")
        self.assertEqual(self.board.winner(), "X")

    """O should win when the left column is filled"""
    def test_column_win(self):
        for i in [0, 3, 6]:
            self.board.set(i, "O")
        self.assertEqual(self.board.winner(), "O")

    """X should win on the main diagonal."""
    def test_diagonal_win(self):
        for i in [0, 4, 8]:
            self.board.set(i, "X")
        self.assertEqual(self.board.winner(), "X")

    """A full board with no winner should return None."""
    def test_tie(self):
        for i, symbol in enumerate(["X", "O", "X", "X", "O", "O", "O", "X", "X"]):
            self.board.set(i, symbol)
        self.assertTrue(self.board.full())
        self.assertIsNone(self.board.winner())

    """A move on an empty square should be valid."""
    def test_valid_move_on_empty_square(self):
        self.assertTrue(self.board.is_valid(4))

    """A move on an occupied square should be invalid."""
    def test_invalid_move_on_occupied_square(self):
        self.board.set(0, "X")
        self.assertFalse(self.board.is_valid(0))

    """A move outside 0-8 should be invalid."""
    def test_invalid_move_out_of_range(self):
        self.assertFalse(self.board.is_valid(9))

"""Tests for the Game class"""
class TestGame(unittest.TestCase):

    """Create a fresh game before each test."""
    def setUp(self):
        self.game = Game()

    """Game should start with Player 1 / symbol=O """
    def test_starts_with_player_one(self):
        self.assertEqual(self.game.current_player().symbol, "O")

    """After one turn, current player should be Player 2 / symbol= X """
    def test_turn_alternates_to_player_two(self):
        self.game.current = 1 - self.game.current
        self.assertEqual(self.game.current_player().symbol, "X")

    """After two turns, current player should return to Player 1 / symbol= O """
    def test_turn_alternates_back_to_player_one(self):
        self.game.current = 1 - self.game.current
        self.game.current = 1 - self.game.current
        self.assertEqual(self.game.current_player().symbol, "O")

    """I use verbosity=2 to get all full details that shows every test name and result"""
if __name__ == "__main__":
    unittest.main(verbosity=2)