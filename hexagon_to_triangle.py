"""
Puzzle | Form Three Equilateral Triangles
Suppose you have a regular hexagon made up of matchsticks with three diagonals in it.
The task is to convert the given hexagon into three equilateral triangles by moving
only 4 matchsticks.
"""

import matplotlib.pyplot as plt
import math

# Function to draw a line (matchstick)
def draw_line(ax, x1, y1, x2, y2, color='gold', lw=3):
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw)

# Function to get hexagon points
def hexagon_points(r=1):
    return [(r * math.cos(math.radians(60 * i)), r * math.sin(math.radians(60 * i))) for i in range(6)]

# Draw the puzzle before and after moving 4 matchsticks
def draw_puzzle():
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    plt.suptitle("Move 4 Matchsticks to Make 3 Equilateral Triangles", fontsize=14)

    # --- Original hexagon ---
    ax = axs[0]
    points = hexagon_points()
    for i in range(6):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 6]
        draw_line(ax, x1, y1, x2, y2)
    
    # Draw diagonals
    draw_line(ax, *points[0], *points[3])
    draw_line(ax, *points[1], *points[4])
    draw_line(ax, *points[2], *points[5])
    
    ax.set_title("Original Hexagon")
    ax.set_aspect('equal')
    ax.axis('off')

    # --- After moving 4 sticks ---
    ax2 = axs[1]
    # New arrangement: 3 equilateral triangles sharing matchsticks
    # Coordinates chosen to form 3 touching triangles
    tri1 = [(0, 0), (1, 0), (0.5, math.sqrt(3)/2)]
    tri2 = [(1, 0), (1.5, math.sqrt(3)/2), (0.5, math.sqrt(3)/2)]
    tri3 = [(0.5, math.sqrt(3)/2), (1.5, math.sqrt(3)/2), (1, math.sqrt(3))]

    triangles = [tri1, tri2, tri3]
    for tri in triangles:
        for i in range(3):
            x1, y1 = tri[i]
            x2, y2 = tri[(i + 1) % 3]
            draw_line(ax2, x1, y1, x2, y2)

    ax2.set_title("After Moving 4 Matchsticks → 3 Equilateral Triangles")
    ax2.set_aspect('equal')
    ax2.axis('off')

    plt.show()

draw_puzzle()
 