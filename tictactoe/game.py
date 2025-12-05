class TicTacToe:
    def __init__(self):
        # Plateau 3x3 initialisé avec des cases vides
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

    def play_move(self, row: int, col: int) -> bool:
        """Joue un coup si la case est libre. Retourne True si le coup est joué, False sinon."""
        if self.winner is not None:
            return False

        if not (0 <= row < 3 and 0 <= col < 3):
            return False

        if self.board[row][col] != " ":
            return False

        self.board[row][col] = self.current_player
        if self.check_winner():
            self.winner = self.current_player
        else:
            if self.is_draw():
                self.winner = "DRAW"
            else:
                self.switch_player()
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self) -> bool:
        b = self.board

        # Lignes
        for row in b:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Colonnes
        for col in range(3):
            if b[0][col] == b[1][col] == b[2][col] != " ":
                return True

        # Diagonales
        if b[0][0] == b[1][1] == b[2][2] != " ":
            return True
        if b[0][2] == b[1][1] == b[2][0] != " ":
            return True

        return False

    def is_draw(self) -> bool:
        # Match nul : plateau plein et pas de gagnant
        if self.check_winner():
            return False
        return all(cell != " " for row in self.board for cell in row)

    def __str__(self) -> str:
        lines = []
        for row in self.board:
            lines.append(" | ".join(row))
        return "\n---------\n".join(lines)


def main():
    game = TicTacToe()
    print("Bienvenue dans le Tic Tac Toe !")
    while game.winner is None:
        print()
        print(game)
        print(f"Au tour de {game.current_player}")
        try:
            coords = input("Entrez ligne et colonne (0,1,2) séparées par un espace: ")
            row_str, col_str = coords.split()
            row, col = int(row_str), int(col_str)
        except ValueError:
            print("Entrée invalide, réessayez.")
            continue

        if not game.play_move(row, col):
            print("Coup invalide, réessayez.")

    print()
    print(game)
    if game.winner == "DRAW":
        print("Match nul !")
    else:
        print(f"Le joueur {game.winner} a gagné !")


if __name__ == "__main__":
    main()
