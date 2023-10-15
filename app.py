import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
MAZE_COLOR = (255, 255, 255)

# Define the player
player_size = 20
player_x = 50
player_y = 50

# Define the maze
maze = [
    "####################",
    "#S#                #",
    "# ###### # # # ### #",
    "#      # # # # #   #",
    "# #### # # # # ### #",
    "# #    #   #   #   #",
    "# # ####### ### # #",
    "#     #         # #",
    "##### ########## # #",
    "#        #    #   #",
    "# ########### #### #",
    "#          #      G#",
    "####################"
]

# Calculate the size of each maze cell
cell_size = min(SCREEN_WIDTH // len(maze[0]), SCREEN_HEIGHT // len(maze))

# Calculate the actual size of the maze
maze_width = cell_size * len(maze[0])
maze_height = cell_size * len(maze)

# Calculate the position to center the maze on the screen
maze_x = (SCREEN_WIDTH - maze_width) // 2
maze_y = (SCREEN_HEIGHT - maze_height) // 2

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Set player movement speed
player_speed = cell_size

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement using arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if maze[player_y // cell_size - 1][player_x // cell_size] != "#":
            player_y -= player_speed
    if keys[pygame.K_DOWN]:
        if maze[(player_y + player_size) // cell_size + 1][player_x // cell_size] != "#":
            player_y += player_speed
    if keys[pygame.K_LEFT]:
        if maze[player_y // cell_size][player_x // cell_size - 1] != "#":
            player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        if maze[player_y // cell_size][(player_x + player_size) // cell_size + 1] != "#":
            player_x += player_speed

    # Ensure the player stays within the maze boundaries
    player_x = max(maze_x, min(player_x, maze_x + maze_width - player_size))
    player_y = max(maze_y, min(player_y, maze_y + maze_height - player_size))

    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the maze
    for row, line in enumerate(maze):
        for col, cell in enumerate(line):
            if cell == "#":
                pygame.draw.rect(screen, MAZE_COLOR, (maze_x + col * cell_size, maze_y + row * cell_size, cell_size, cell_size))

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_size, player_size))

    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
