# ===========================
# geometry.py (FINAL FIX WITH HOVER PREVIEW + COLOR CHANGE)
# ===========================
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from config import *

# Define full tailgate and window border points (dense)
def create_border_points(x, y, width, height, num_points=100):
    top = np.linspace([x, y + height], [x + width, y + height], num_points)
    bottom = np.linspace([x, y], [x + width, y], num_points)
    left = np.linspace([x, y], [x, y + height], num_points)
    right = np.linspace([x + width, y], [x + width, y + height], num_points)
    return np.vstack((top, right, bottom[::-1], left[::-1]))

tailgate_border = create_border_points(0, 0, TAILGATE_WIDTH, TAILGATE_HEIGHT)
window_border = create_border_points(NOMINAL_GAP, NOMINAL_GAP, WINDOW_WIDTH, WINDOW_HEIGHT)

def snap_to_nearest_border(click_point, border_points, threshold=20):
    click_point = np.array(click_point)
    dists = np.linalg.norm(border_points - click_point, axis=1)
    min_dist_idx = np.argmin(dists)
    if dists[min_dist_idx] < threshold:
        return border_points[min_dist_idx]
    else:
        return None

def draw_geometry_with_gap():
    fig, ax = plt.subplots(figsize=(10, 5))

    tailgate = patches.FancyBboxPatch((0, 0), TAILGATE_WIDTH, TAILGATE_HEIGHT,
        boxstyle="round,pad=0.02,rounding_size=20", edgecolor='black', facecolor='lightgrey', linewidth=2, label="Tailgate")
    ax.add_patch(tailgate)

    window = patches.FancyBboxPatch((NOMINAL_GAP, NOMINAL_GAP), WINDOW_WIDTH, WINDOW_HEIGHT,
        boxstyle="round,pad=0.02,rounding_size=15", edgecolor='blue', facecolor='skyblue', linewidth=2, label="Window")
    ax.add_patch(window)

    gap_color = 'red'
    gap_alpha = 0.2
    ax.add_patch(patches.Rectangle((0, NOMINAL_GAP), NOMINAL_GAP, WINDOW_HEIGHT, color=gap_color, alpha=gap_alpha))
    ax.add_patch(patches.Rectangle((NOMINAL_GAP + WINDOW_WIDTH, NOMINAL_GAP), NOMINAL_GAP, WINDOW_HEIGHT, color=gap_color, alpha=gap_alpha))
    ax.add_patch(patches.Rectangle((NOMINAL_GAP, 0), WINDOW_WIDTH, NOMINAL_GAP, color=gap_color, alpha=gap_alpha))
    ax.add_patch(patches.Rectangle((NOMINAL_GAP, NOMINAL_GAP + WINDOW_HEIGHT), WINDOW_WIDTH, NOMINAL_GAP, color=gap_color, alpha=gap_alpha))

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

def draw_gap_between_points(tailgate_point, window_point, tailgate_tol_value, window_tol_value):
    tailgate_actual = (tailgate_point[0] + tailgate_tol_value, tailgate_point[1] + tailgate_tol_value)
    window_actual = (window_point[0] + window_tol_value, window_point[1] + window_tol_value)

    distance = np.sqrt((tailgate_actual[0] - window_actual[0])**2 + (tailgate_actual[1] - window_actual[1])**2)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.add_patch(patches.Rectangle((0, 0), TAILGATE_WIDTH, TAILGATE_HEIGHT, edgecolor='orange', facecolor='lightgrey', linewidth=3, label='Tailgate'))
    ax.add_patch(patches.Rectangle((NOMINAL_GAP, NOMINAL_GAP), WINDOW_WIDTH, WINDOW_HEIGHT, edgecolor='purple', facecolor='skyblue', linewidth=3, label='Window'))

    ax.plot(*tailgate_actual, 'ro', label='Tailgate Point')
    ax.plot(*window_actual, 'go', label='Window Point')
    ax.plot([tailgate_actual[0], window_actual[0]], [tailgate_actual[1], window_actual[1]], 'r--')

    ax.text((tailgate_actual[0] + window_actual[0])/2, (tailgate_actual[1] + window_actual[1])/2 + 10,
            f"Gap = {distance:.2f} mm", color='red', fontsize=10)

    ax.set_xlim(-20, TAILGATE_WIDTH + 50)
    ax.set_ylim(-20, TAILGATE_HEIGHT + 50)
    ax.set_aspect('equal')
    ax.set_title("Gap Between Selected Points (with Tolerances)")
    ax.legend()
    plt.grid(True)
    plt.show()

    return distance

def select_and_measure_gap():
    fig, ax = plt.subplots(figsize=(10, 5))
    tailgate_rect = patches.Rectangle((0, 0), TAILGATE_WIDTH, TAILGATE_HEIGHT, edgecolor='orange', facecolor='lightgrey', linewidth=3, label='Tailgate')
    window_rect = patches.Rectangle((NOMINAL_GAP, NOMINAL_GAP), WINDOW_WIDTH, WINDOW_HEIGHT, edgecolor='purple', facecolor='skyblue', linewidth=3, label='Window')

    ax.add_patch(tailgate_rect)
    ax.add_patch(window_rect)

    ax.set_xlim(-20, TAILGATE_WIDTH + 50)
    ax.set_ylim(-20, TAILGATE_HEIGHT + 50)
    ax.set_aspect('equal')
    ax.set_title("Hover and Click: Tailgate (Orange) then Window (Purple)")
    plt.grid(True)
    plt.legend()

    hover_dot, = ax.plot([], [], 'yo', markersize=8, alpha=0.7)  # Dynamic hover point

    state = {'selecting': 'tailgate'}

    def on_mouse_move(event):
        if not event.inaxes:
            return
        if state['selecting'] == 'tailgate':
            snapped = snap_to_nearest_border([event.xdata, event.ydata], tailgate_border)
            hover_dot.set_color('orange')
        else:
            snapped = snap_to_nearest_border([event.xdata, event.ydata], window_border)
            hover_dot.set_color('purple')

        if snapped is not None:
            hover_dot.set_data([snapped[0]], [snapped[1]])
            hover_dot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            hover_dot.set_visible(False)
            fig.canvas.draw_idle()

    cid = fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)

    print("Hover and click near Tailgate border...")
    tailgate_click = plt.ginput(1, timeout=30)[0]
    snapped_tailgate = snap_to_nearest_border(tailgate_click, tailgate_border)

    if snapped_tailgate is None:
        print("First click not close to Tailgate border. Try again.")
        plt.close(fig)
        return

    state['selecting'] = 'window'
    print("Hover and click near Window border...")
    window_click = plt.ginput(1, timeout=30)[0]
    snapped_window = snap_to_nearest_border(window_click, window_border)

    if snapped_window is None:
        print("Second click not close to Window border. Try again.")
        plt.close(fig)
        return

    plt.close(fig)

    tailgate_tol_value = np.random.normal(0, TAILGATE_TOL)
    window_tol_value = np.random.normal(0, WINDOW_TOL)

    draw_gap_between_points(snapped_tailgate, snapped_window, tailgate_tol_value, window_tol_value)
