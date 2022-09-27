from .team import Team
import pygame

PYGAME_HEIGHT = 600
PYGAME_WIDTH = 800
PYGAME_BORDER = 50

class Board:

  def __init__(self, board_size):
    self.board_size = board_size
    nb_pieces = int((board_size / 2) * ((board_size / 2) - 1))

    length = (PYGAME_HEIGHT - 2 * PYGAME_BORDER) / self.board_size

    self.white_team = Team(
      int(((board_size * board_size) / 2) - nb_pieces + 1), 
      int((board_size * board_size) / 2) + 1,
      self.board_size,
      length,
      PYGAME_BORDER
    )
    self.black_team = Team(
      1, 
      nb_pieces + 1,
      self.board_size,
      length,
      PYGAME_BORDER
    )

    print(f'Number of pieces for each team : {nb_pieces}')
    print(self.black_team)
    print(self.white_team)

  def draw_board(self, screen):
    screen.fill((28, 32, 33))
    length = (PYGAME_HEIGHT - 2 * PYGAME_BORDER) / self.board_size
    for i in range(self.board_size):
      for j in range(self.board_size):
        x = PYGAME_BORDER + (i * length)
        y = PYGAME_BORDER + (j * length)
        rect = pygame.Rect(x, y, length, length)
        pygame.draw.rect(
          screen, 
          (232, 233, 235) if 
            (i % 2 == 0 and j % 2 == 0) or 
            (i % 2 == 1 and j % 2 == 1) 
            else (186, 96, 18),
          rect
        )

    pygame.display.flip()

  def draw_pieces(self, screen):
    length = (PYGAME_HEIGHT - 2 * PYGAME_BORDER) / self.board_size
    # White team
    for piece in self.black_team.getPieces():
      pygame.draw.rect(
          screen, 
          (0, 0, 0),
          piece.getRect(),
          border_radius=int(length)
        )
      '''x = (((piece.getPosition() - 1) % (self.board_size // 2)) + 1) * 2 - 1 - (1 if (piece.getPosition() - 1) % self.board_size >= self.board_size // 2 else 0)
      y = (piece.getPosition() - 1) // (self.board_size // 2)

      pygame.draw.circle(
        screen,
        (255, 255, 255),
        [PYGAME_BORDER + (length / 2) + (x * length), PYGAME_BORDER + (length / 2) + (y * length)],
        length / 3
      )'''

    # Black team
    for piece in self.white_team.getPieces():
      pygame.draw.rect(
          screen, 
          (255, 255, 255),
          piece.getRect(),
          border_radius=int(length)
        )

    pygame.display.flip()

  def run(self):

    # Initialize the library
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([PYGAME_WIDTH, PYGAME_HEIGHT])

    # Draw the board
    self.draw_board(screen)

    # Draw pieces
    self.draw_pieces(screen)

    running = True
    while running:

      for event in pygame.event.get():

        # If the user closes the drawed window, quit the program
        if event.type == pygame.QUIT:
          running = False

        # if the user is clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
          for team in [self.white_team, self.black_team]:
            for piece in team.getPieces():
              if piece.getRect().collidepoint(pos):
                print(piece)

        # if the user finished click
        if event.type == pygame.MOUSEBUTTONUP:
          print('wow')

    pygame.quit()


