from .piece import Piece

class Team:

  def __init__(self, posStart, posEnd, board_size, length, border):
    self.pieces = []
    for pos in range(posStart, posEnd):
      x = (((pos - 1) % (board_size // 2)) + 1) * 2 - 1 - (1 if (pos - 1) % board_size >= board_size // 2 else 0)
      y = (pos - 1) // (board_size // 2)
      print(x, y)
      self.pieces.append(
        Piece(
          pos, 
          border + (length / 8) + (x * length),
          border + (length / 8) + (y * length), 
          length - (2 * (length / 8))
        )
      )

  def __str__(self):
    res = ''
    for piece in self.pieces:
      res += str(piece) + ' '

    return res

  def getPieces(self):
    return self.pieces