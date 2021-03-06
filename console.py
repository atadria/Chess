#!/usr/bin/env python3

from piece import *
from color import Color

piece_to_value = { Pawn: 1, Rook: 2, Knight: 3, Bishop: 4, Queen: 5, King: 6 }

number_to_char = { 0: ' ', 1: 'p', 2: 'r', 3: 'n', 4: 'b', 5: 'q', 6: 'k' }

color_to_name = {Color.White: "WHITE", Color.Black: "BLACK"}

class Console:
    def __init__(self):
        self._data = []

    def visit(self, values):
        self._data = values

    def draw(self):
        """Wyświetla szachownicę"""
        self._show_column_names()
        for row in range(8):
            self._show_row_separator()
            self._show_row(row)
        self._show_row_separator()
        self._show_column_names()

    def illegal_move_error(self):
        print("Illegal move error! Try again.")

    def show_player_info(self, name, color):
        """Wyświetla informację na temat gracza"""
        print("Player: %s, plays: %s" % (name, color_to_name[color]), end='')

    def input_move(self):
        """Wprowadza ruch z konsoli"""
        return input(" move: ")

    def _show_column_names(self):
        """Wyświetla nazwy kolumn"""
        print("   a b c d e f g h")

    def _show_row_separator(self):
        """Wyświetla separator wierszy"""
        print("  ", "+-" * 8, '+', sep='')

    def _show_row(self, row):
        """Wyświetla pełen wiersz z figurami"""
        print(8 - row, end=' ')
        for col in range(8):
            value = self._data[row][col]
            rpr = number_to_char[value if value < 100 else value - 100]
            if value < 100:
                rpr = rpr.upper()
            print('|', rpr, sep='', end='')
        print('|', 8 - row)
