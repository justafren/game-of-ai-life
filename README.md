https://chat.openai.com/share/e1ac65cb-3fde-4d63-993a-019db0d5223f


# Game of Life

This is a Python program based on Conway's Game of Life, implemented with a GUI interface using the `pygame` library. The Game of Life is a cellular automaton devised by the mathematician John Conway.

## How to Run

1. Make sure you have Python installed on your system (version 3.6 or above).

2. Clone this repository or download the source code files.

3. Install the required dependencies by running the following command:

pip install -r requirements.txt

4. Choose the version of the program you want to run:

- For the version that updates the grid with one iteration per Enter key press, run the following command:

  ```
  python game_of_life.py
  ```

- For the version that updates the grid continuously until there is no more movement, run the following command:

  ```
  python game_of_life_play.py
  ```

Both commands will launch the Game of Life program with a graphical window.

## How to Play

1. Upon running the program, a window will appear with a grid representing the Game of Life world.

2. To add "alive" cells, click on the grid. Each click will toggle the state of the cell between alive and dead.

3. Press the Enter key to update the grid based on the Game of Life rules. In the first version, the grid will be updated with one iteration per Enter key press. In the second version, the grid will be updated continuously until there is no more movement.

4. Observe the patterns and behavior of the cells as they evolve. In the second version, you can pause the simulation by pressing the Enter key again.

5. To exit the program, simply close the window or press the close button.

## Customize the Game

You can modify the program code to customize various aspects of the Game of Life:

- Adjust the `WINDOW_WIDTH` and `WINDOW_HEIGHT` constants in the code to change the size of the graphical window.

- Modify the `CELL_SIZE` constant to adjust the size of individual cells in the grid.

- Change the colors used for the grid and cells by modifying the color constants defined in the code.

- Adjust the tick rate in the game loop (`clock.tick(10)`) to control the speed of the simulation in the second version.

Feel free to experiment and explore different patterns and configurations within the Game of Life!