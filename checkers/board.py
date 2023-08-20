import pygame
from .constants import BLACK, ROWS, IVORY_WHITE, SQUARE_SIZE, COLS, WHITE
from .piece import Piece

class Board:
    """ Control the board and piece behavior, including valid move sets."""

    def __init__(self) -> None:
        """initialize board, pieces remaining, kings and board."""
        # internal representation of the board
        self.board = []
        self.white_remaining = self.black_remaining = 12
        self.white_kings = self.black_kings = 0
        self.create_board()
    
    # draw checkerboard
    def draw_board_squares(self, window):
        """draw checkerboard."""
        window.fill(BLACK)
        for row in range(ROWS):
            # draws square every two squares and in each row. think of col as a square that is drawn
            for col in range(row % 2, ROWS, 2):
                # draws rectangle in white
                # rect argument specifies dimensions
                pygame.draw.rect(window, IVORY_WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # initalizes it
    def create_board(self):
        """create internal representation of piece."""
        for row in range(ROWS):
            # creates list in each row (contains empty and occupied spaces)
            self.board.append([])
            for col in range(COLS):
                # smth
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        # draw piece
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        # blank pieces. act as separators in list
                        self.board[row].append(0)
                else:
                    # no pieces added
                    self.board[row].append(0)
    
    # draws board AND pieces
    def draw_board_and_pieces(self, window):
        """draw visual representation of checkerboard and pieces."""
        self.draw_board_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(window)
    
    def remove(self, pieces):
        """remove piece."""
        # pieces are technically still there but there is no visual representation
        # a 'removed' piece is set to 0 
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.black_remaining -= 1
                else:
                    self.white_remaining -= 1

    def winner(self):
        """return winner."""
        if self.black_remaining <= 0:
            return WHITE
        elif self.white_remaining <= 0:
            return BLACK

        return None 
    def move(self, piece, row, col):
        """move piece and change its position."""
        # easy way to swap positions in a list in python!!
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1

    # gets position of piece
    def get_piece(self, row, col):
        """get piece position."""
        return self.board[row][col]
    
    def get_valid_moves(self, piece):
        """get valid moves and update moveset based on color or king status."""
        # valid square: pieces we jump over eg. (4,5): [(3,4)]
        # stored in list in valid_moves dict
        # when piece moves to valid square, the jumped piece is removed in list
        # the list can contain nothing, which means a piece can just move to a valid square eg. (4,5): []
        valid_moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # checks what way a piece can move based on color or king status
        # returns dict
        # max(row - 3, -1) looks for moves that can jump over a piece *or* just move left if there is no piece there
        # -1 in max() means the top row of the board; meaning pieces stop before that point
        # -1 passed as step variable increments for loop in traverse left method
        if piece.color == BLACK or piece.king:
            valid_moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            valid_moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        # ROWS in min() means the last row at the bottom of the board; meaning pieces stop before that point
        if piece.color == WHITE or piece.king:
            valid_moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            valid_moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return valid_moves
    
    # traverse left and right account for the multiple jumps
    # step will be dependent on direction of movement (up or down if king)
    # skipped contains jumped pieces; "we can only move to squares when we skip another piece"
    # skipped is initalized to an empty list so that one piece's moves don't carry over into another's
    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        """look for valid moves on the left side the selected piece can make."""
        moves = {}
        last = []
        # this for loop constantly checks to see if it can add to moves which will then be added to valid moves
        for r in range(start, stop, step):
            # if piece reaches left edge of board, will not be added to valid moves
            if left < 0:
                break
            
            # THIS IS NOT the piece itself, but rather the square being looked at 
            # this is to determine if it can be added to valid moves
            current_position = self.board[r][left]

            # breaks out of for loop if a piece has been skipped
            # if == 0, piece has found empty square
            if current_position == 0:
                # this is the case when skipped is last but are 2 different things at this point
                if skipped and not last:
                    break
                elif skipped:
                    # adds to jump, making it double jump
                    moves[(r, left)] = last + skipped 
                else:
                    # if above is not true
                    # when there is no piece to skip over, this position in variable moves[(r, left)]
                    # will be stored as the last possible move a piece can make and be added to moves list
                    moves[(r, left)] = last
                
                # checks to see if we can double jump or not
                # if not, last row is the last possible move
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    # checks to see if we can double or triple jump below
                    # r + step looks for the next row up, step makes it diagonal, left - 1 shifts to the left and vice versa
                    # skipped = last means when a piece has jumped over opponent's piece, this is the last move they can do
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped = last))
                    # sometimes a piece can double jump and this may involve them jumping to the left 
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped = last))
                break

            # if current position does not equal and the piece occupying it is the same color
            # this will not be part of moves dict/break out of for loop
            elif current_position.color == color:
                break
            # if not player's color, it is opponent's color
            # last will then be the last move a piece can make before the next person's turn
            else:
                last = [current_position]
            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        """look for valid moves on the right side the selected piece can make."""
        moves = {}
        last = []
        # this for loop constantly checks to see if it can add to moves which will then be added to valid moves
        for r in range(start, stop, step):
            # if piece reaches left edge of board, will not be added to valid moves
            if right >= COLS:
                break
            
            # THIS IS NOT the piece itself, but rather the square being looked at 
            # this is to determine if it can be added to valid moves
            current_position = self.board[r][right]

            # breaks out of for loop if a piece has been skipped
            # if == 0, piece has found empty square
            if current_position == 0:
                if skipped and not last:
                    break
                elif skipped:
                    # adds to jump, making it double jump
                    moves[(r, right)] = last + skipped 
                else:
                    # if above is not true
                    # when there is no piece to skip over, this position in variable moves[(r, left)]
                    # will be stored as the last possible move a piece can make and be added to moves list
                    moves[(r, right)] = last
                
                # checks to see if we can double jump or not
                # if not, last row is the last possible move
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped = last))
                    # sometimes a piece can double jump and this may involve them jumping to the left
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped = last))
                break

            # if current position does not equal and the piece occupying it is the same color
            # this will not be part of moves dict/break out of for loop
            elif current_position.color == color:
                break
            # if not player's color, it is opponent's color
            # last will then be the last move a piece can make before the next person's turn
            else:
                last = [current_position]
            right += 1

        return moves