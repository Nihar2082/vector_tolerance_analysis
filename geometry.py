## geometry.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from config import *

def draw_geometry_with_gap():
    fig, ax = plt.subplots(figsize=(10, 5))

    # Tailgate (rectangle with corner radius effect)
    tailgate = patches.FancyBboxPatch(
        (0, 0), TAILGATE_WIDTH, TAILGATE_HEIGHT,
        boxstyle="round,pad=0.02,rounding_size=20",
        edgecolor='black', facecolor='lightgrey', linewidth=2, label="Tailgate"
    )
    ax.add_patch(tailgate)

    # Window (rectangle with corner radius effect)
    window = patches.FancyBboxPatch(
        (NOMINAL_GAP, NOMINAL_GAP), WINDOW_WIDTH, WINDOW_HEIGHT,
        boxstyle="round,pad=0.02,rounding_size=15",
        edgecolor='blue', facecolor='skyblue', linewidth=2, label="Window"
    )
    ax.add_patch(window)

    # Gap area (4 sides)
    gap_color = 'red'
    gap_alpha = 0.2
    ax.add_patch(patches.Rectangle((0, NOMINAL_GAP), NOMINAL_GAP, WINDOW_HEIGHT, color=gap_color, alpha=gap_alpha))
    ax.add_patch(patches.Rectangle((NOMINAL_GAP + WINDOW_WIDTH, NOMINAL_GAP), NOMINAL_GAP, WINDOW_HEIGHT, color=gap_color, alpha=gap_alpha))
    ax.add_patch(patches.Rectangle((NOMINAL_GAP, 0), WINDOW_WIDTH, NOMINAL_GAP, color=gap_color, alpha=gap_alpha))
    ax.add_patch(patches.Rectangle((NOMINAL_GAP, NOMINAL_GAP + WINDOW_HEIGHT), WINDOW_WIDTH, NOMINAL_GAP, color=gap_color, alpha=gap_alpha))

    # Labels
    ax.text(5, TAILGATE_HEIGHT/2, "Left Gap", va='center', color='red', fontsize=9, rotation=90)
    ax.text(TAILGATE_WIDTH - 15, TAILGATE_HEIGHT/2, "Right Gap", va='center', color='red', fontsize=9, rotation=90)
    ax.text(TAILGATE_WIDTH/2, 5, "Bottom Gap", ha='center', color='red', fontsize=9)
    ax.text(TAILGATE_WIDTH/2, TAILGATE_HEIGHT - 15, "Top Gap", ha='center', color='red', fontsize=9)

    ax.set_xlim(-20, TAILGATE_WIDTH + 20)
    ax.set_ylim(-20, TAILGATE_HEIGHT + 20)
    ax.set_aspect('equal')
    ax.set_title("Tailgate and Window with Visualized Gaps")
    ax.legend()
    plt.grid(True)
    plt.show()
 