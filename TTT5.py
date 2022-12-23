import pygame

# Initialize the game board
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

# Function for drawing a line on the game board for the winning tiles
def draw_line(board, line, screen, color):
    for i in range(3):
        x = 150 + line[i][1] * 150
        y = 150 + line[i][0] * 150
        pygame.draw.rect(screen, color, (x, y, 150, 150)) 

# Function for checking if a player has won the game
def check_win(board, screen, color):
    # Check for horizontal wins
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            draw_line(board, [[i,0], [i,1], [i,2]], screen, color)
            return True
    # Check for vertical wins
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            draw_line(board, [[0,i], [1,i], [2,i]], screen, color)
            return True
    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        draw_line(board, [[0,0], [1,1], [2,2]], screen, color)
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        draw_line(board, [[0,2], [1,1], [2,0]], screen, color)
        return
    return False

# Function for checking if the game is a draw
def check_draw(board):
    for row in board:
        if "_" in row:
            return False
    return True

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((750, 800))

# Set the window title
pygame.display.set_caption("Tic-Tac-Toe")

# Set the colors
BLACK = (71, 61, 93)
WHITE = (243, 235, 217)
BLUE = (5, 142, 217)
DARK_GRAY = (71, 61, 93)
LIGHT_GRAY = (163, 154, 146)

# Initialize the game
running = True
player = "X"

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            x, y = pygame.mouse.get_pos()

            # Calculate the row and column of the click
            row = (y - 150) // 150
            col = (x - 150) // 150

            # Check if the click was on the game board
            if row >= 0 and row <= 2 and col >= 0 and col <= 2:
                # Check if the square is empty
                if board[row][col] == "_":
                    # Make the player's move
                    board[row][col] = player

                    # Switch players
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"

    # Clear the screen
    screen.fill(BLACK)

    # Draw the game board
    for i in range(3):
        for j in range(3):
            x = 150 + j * 150
            y = 150 + i * 150
            pygame.draw.rect(screen, WHITE, (x, y, 150, 150), 5)
            if board[i][j] == "X":
                pygame.draw.line(screen, BLUE, (x, y), (x + 150, y + 150), 5)
                pygame.draw.line(screen, BLUE, (x + 150, y), (x, y + 150), 5)
            elif board[i][j] == "O":
                pygame.draw.circle(screen, BLUE, (x + 75, y + 75), 75, 5)

    # Check if the player has won
    if check_win(board, screen, BLUE):
        pass

    # Check if the game is a draw
    if check_draw(board):
        pass

    # Draw the "Play again" button
    pygame.draw.rect(screen, LIGHT_GRAY, (150, 600, 450, 100))
    font = pygame.font.Font(None, 50)
    text = font.render("Play again", True, DARK_GRAY)
    text_rect = text.get_rect()
    text_rect.center = (375, 650)
    screen.blit(text, text_rect)

    # Check if the "Play again" button is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 150 <= x <= 550 and 600 <= y <= 700:
            board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    # Update the screen
    pygame.display.flip()

# Close the window
pygame.quit()
