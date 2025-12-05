from tictactoe.game import TicTacToe


def test_first_player_is_X():
    game = TicTacToe()
    assert game.current_player == "X"