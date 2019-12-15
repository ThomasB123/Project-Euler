# Lattice paths
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''
# Answer = 137846528820

# is basically a problem of arranging the moves in different orders:
# e.g. a 2x2 grid:
# right right down down
# right down right down
# right down down right
# down right down right
# down right right down
# down down right right

# can think of it as just where to place the 2 rights in the 4 moves.
# for 2*2 grid, answer is 4 choose 2

# for 20*20 grid, answer is 40 choose 20
# 40!/(20!*20!)
import math
print(int(math.factorial(40)/math.factorial(20)**2))