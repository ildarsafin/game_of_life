import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
  def __init__(self, size, updateInterval):
    LIFE = 255
    DEATH = 0
    self.vals = [LIFE, DEATH]

    self.size = size
    self.updateInterval = updateInterval
    self.grid = self.generateGrid(self.size, self.vals)

    self.animate(self.grid, size)

  def generateGrid(self, size, vals):
    return np.random.choice(vals, size*size, p=[0.1, 0.9]).reshape(size, size)

  def animate(self, grid, size):
    figure, axis = plt.subplots()
    image = axis.imshow(grid, interpolation='nearest')
    animationObj = animation.FuncAnimation(figure, self.update,
                                  fargs=(image, grid, size),
                                  interval=self.updateInterval)

    plt.show()

  def update(self, _, image, grid, size):
    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    tempGrid = grid.copy()
    for i in range(size):
      for j in range(size):
        # compute 8-neghbor sum
        neighborSum = int((grid[i, (j-1) % size] + grid[i, (j+1) % size] +
                     grid[(i-1) % size, j] + grid[(i+1) % size, j] +
                     grid[(i-1) % size, (j-1) % size] + grid[(i-1) % size, (j+1) % size] +
                     grid[(i+1) % size, (j-1) % size] + grid[(i+1) % size, (j+1) % size]) / 255)

        # apply Conway's rules
        if grid[i, j] == self.vals[0]:
          if (neighborSum < 2) or (neighborSum > 3):
            tempGrid[i, j] = self.vals[1]
        else:
          if neighborSum == 3:
            tempGrid[i, j] = self.vals[0]

    grid[:] = tempGrid[:]
    image.set_data(grid)

    return image

GameOfLife(100, 50)
