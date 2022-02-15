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
    All moves without checks possibilities
    """

    def get_all_possible_move(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                type = self.board[row][col][0]
                if (type == 'w' and self.whiteToMove) or (type == 'b' and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    if piece == 'p':
                        self.get_pawn_move(row, col, moves)
                    elif piece == 'R':
                        self.get_rock_move(row, col, moves)
                    elif piece == 'R':
                        self.get_bishop_move(row, col, moves)
                    elif piece == 'R':
                        self.getKnightMove(row, col, moves)
                    elif piece == 'R':
                        self.getQueenMove(row, col, moves)
                    elif piece == 'R':
                        self.getKingMove(row, col, moves)
        return moves

    """
    Movement of all pieces in Chess
    """

    def get_pawn_move(self, row, col, moves):




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

    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startCol) + self.get_rank_file(self.endRow, self.endCol)

    def get_rank_file(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
