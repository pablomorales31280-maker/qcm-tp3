import pytest
import os
import sys

# Ajouter le dossier parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tictactoe.game import TicTacToe




def test_initial_state():
    game = TicTacToe()
    # Joueur X commence
    assert game.current_player == "X"
    # Personne n'a gagné au début
    assert game.winner is None
    # Plateau vide
    for row in game.board:
        assert row == [" ", " ", " "]


def test_valid_move_places_symbol_and_switches_player():
    game = TicTacToe()

    played = game.play_move(0, 0)

    assert played is True
    assert game.board[0][0] == "X"
    # Après un coup valide, on change de joueur
    assert game.current_player == "O"

    def test_player_alternates_correctly():
        game = TicTacToe()

        game.play_move(0, 0)  # X plays
        assert game.current_player == "O"
        
        game.play_move(1, 0)  # O plays
        assert game.current_player == "X"

def test_cannot_play_out_of_bounds():
    game = TicTacToe()

    played = game.play_move(3, 3)  # en dehors du plateau 3x3

    assert played is False
    # Plateau toujours vide
    for row in game.board:
        assert row == [" ", " ", " "]


def test_cannot_play_on_occupied_cell():
    game = TicTacToe()

    first = game.play_move(0, 0)
    second = game.play_move(0, 0)  # même case

    assert first is True
    assert second is False
    # La case contient toujours le premier symbole
    assert game.board[0][0] == "X"


def test_win_on_row_sets_winner_and_stops_game():
    game = TicTacToe()

    # X va gagner sur la première ligne
    game.play_move(0, 0)  # X
    game.play_move(1, 0)  # O
    game.play_move(0, 1)  # X
    game.play_move(1, 1)  # O
    game.play_move(0, 2)  # X gagne

    assert game.winner == "X"
    # Après qu'il y ait un gagnant, plus aucun coup ne doit être joué
    played_after_win = game.play_move(2, 2)
    assert played_after_win is False
    assert game.board[2][2] == " "


def test_draw_game_sets_winner_to_draw():
    game = TicTacToe()

    # Séquence qui mène à un match nul (pas de gagnant)
    moves = [
        (0, 0), (0, 1),
        (0, 2), (1, 1),
        (1, 0), (1, 2),
        (2, 1), (2, 0),
        (2, 2),
    ]

    for row, col in moves:
        assert game.play_move(row, col) is True

    assert game.winner == "DRAW"
    # Plus de coup possible après un match nul
    assert game.play_move(0, 0) is False


def test_str_representation_not_empty():
    game = TicTacToe()

    s = str(game)

    # Il doit y avoir au moins une ligne et des séparateurs
    assert isinstance(s, str)
    assert " | " in s
    assert "---------" in s
