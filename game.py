import math
import time
from Player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self._make_board()
        self.current_winner = None

    def _make_board(self):
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self._winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def _winner(self, square, letter):
        row_ind = square // 3
        if all([s == letter for s in self.board[row_ind * 3:(row_ind + 1) * 3]]):
            return True
        col_ind = square % 3
        if all([s == letter for s in [self.board[col_ind + i * 3] for i in range(3)]]):
            return True
        if square % 2 == 0:
            if all([self.board[i] == letter for i in [0, 4, 8]]) or all([self.board[i] == letter for i in [2, 4, 6]]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play_game(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    game = TicTacToe()
    play_game(game, x_player, o_player, print_game=True)