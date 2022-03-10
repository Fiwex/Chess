"""
Class for keep data and board related analysis
"""


class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []
        self.whiteCanCastle = True
        self.blackCanCastle = True

    def make_move(self, move):
        if (self.whiteToMove and self.board[move.startRow][move.startCol][0] != "w") or \
                (not self.whiteToMove and self.board[move.startRow][move.startCol][0] != "b"):
            return  # Check if the right player is playing
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove  # switch turn

    def undo_move(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    """
    All moves considering checks
    """
    def get_valid_moves(self):
        return self.get_all_possible_move()

    """
    All moves without checks
    """
    def get_all_possible_move(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                color = self.board[row][col][0]
                if (color == 'w' and self.whiteToMove) or (color == 'b' and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    if piece == 'p':
                        self.get_pawn_move(row, col, moves)
                    elif piece == 'R':
                        self.get_rock_move(row, col, moves)
                    elif piece == 'B':
                        self.get_bishop_move(row, col, moves)
                    elif piece == 'N':
                        self.get_knight_move(row, col, moves)
                    elif piece == 'Q':
                        self.get_queen_move(row, col, moves)
                    elif piece == 'K':
                        self.get_king_move(row, col, moves)
        return moves

    """
    Movement of all pieces in Chess
    """

    def get_pawn_move(self, row, col, moves):
        if self.whiteToMove:  # because pawns are direction specific
            if self.board[row - 1][col] == "--":  # front square is empty
                moves.append(Move((row, col), (row - 1, col), self.board))
                if row == 6 and self.board[row - 2][col] == "--":
                    moves.append(Move((row, col), (row - 2, col), self.board))

        else:
            if self.board[row + 1][col] == "--":
                moves.append(Move((row, col), (row + 1, col), self.board))
                if row == 1 and self.board[row + 2][col] == "--":
                    moves.append(Move((row, col), (row + 2, col), self.board))

    def get_rock_move(self, row, col, moves):
        pass

    def get_bishop_move(self, row, col, moves):
        pass

    def get_knight_move(self, row, col, moves):
        pass

    def get_queen_move(self, row, col, moves):
        pass

    def get_king_move(self, row, col, moves):
        pass


class Move:
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, start_sq, end_sq, board):
        self.startRow = start_sq[0]
        self.startCol = start_sq[1]
        self.endRow = end_sq[0]
        self.endCol = end_sq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol  # Small hash-like
        # function for all move in check

    """
    Overriding equals method
    """
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startCol) + self.get_rank_file(self.endRow, self.endCol)

    def get_rank_file(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
