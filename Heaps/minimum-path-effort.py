

# You are a hiker preparing for an upcoming hike. You are given heights,
#   a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col).
#   You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell,
#   (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find
#   a route that requires the minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# Notes:
#   Matrix can have unequal number of rows and columns (not square)
#   If the height of an adjacent cell is less than the current cell, that number is subtracted

# todo: this is a graph problem

def minimum_path_effort(heights):
    rows = len(heights)
    cols = len(heights[0])
