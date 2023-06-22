import pygame
import numpy as np

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Grid dimensions
GRID_SIZE = 20
CELL_SIZE = 20

# Initialize the grid
grid_width = WINDOW_WIDTH // CELL_SIZE
grid_height = WINDOW_HEIGHT // CELL_SIZE
grid = np.zeros((grid_width, grid_height), dtype=bool)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

# Function to draw the grid
def draw_grid():
    window.fill(BLACK)
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(window, WHITE, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(window, WHITE, (0, y), (WINDOW_WIDTH, y))

    for x in range(grid_width):
        for y in range(grid_height):
            if grid[x, y]:
                pygame.draw.rect(window, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to update the grid based on the Game of Life rules
def update_grid():
    new_grid = np.copy(grid)
    for x in range(grid_width):
        for y in range(grid_height):
            neighbors = np.sum(grid[max(0, x-1):min(x+2, grid_width), max(0, y-1):min(y+2, grid_height)]) - grid[x, y]
            if grid[x, y] and (neighbors < 2 or neighbors > 3):
                new_grid[x, y] = False
            elif not grid[x, y] and neighbors == 3:
                new_grid[x, y] = True
    return new_grid

# Game loop
running = True
drawing = False
game_running = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            game_running = True

        if drawing:
            pos = pygame.mouse.get_pos()
            x = pos[0] // CELL_SIZE
            y = pos[1] // CELL_SIZE
            grid[x, y] = True

    if game_running:
        new_grid = update_grid()
        if np.array_equal(grid, new_grid):
            game_running = False
        grid = new_grid

    draw_grid()

    pygame.display.flip()
    clock.tick(10)  # Adjust the tick rate to change the speed of the game

# Quit the program
pygame.quit()