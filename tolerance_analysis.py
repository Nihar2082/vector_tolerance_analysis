# tolerance_analysis.py

import numpy as np
import matplotlib.pyplot as plt
from config import *

def simulate_tolerances():
    np.random.seed(42)
    tailgate_tol = np.random.normal(0, TAILGATE_TOL, NUM_SAMPLES)
    window_tol = np.random.normal(0, WINDOW_TOL, NUM_SAMPLES)

    final_tailgate_w = TAILGATE_WIDTH + tailgate_tol
    final_window_w = WINDOW_WIDTH + window_tol

    final_tailgate_h = TAILGATE_HEIGHT + tailgate_tol
    final_window_h = WINDOW_HEIGHT + window_tol

    gap_w = final_tailgate_w - final_window_w
    gap_h = final_tailgate_h - final_window_h

    return gap_w, gap_h

def plot_gap_histograms(gap_w, gap_h):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.hist(gap_w, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.axvline(x=2*NOMINAL_GAP, color='red', linestyle='dashed', label="Nominal Gap (20 mm)")
    plt.xlabel("Gap in Width (mm)")
    plt.ylabel("Frequency")
    plt.title("Tolerance Analysis - Width Gap")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.hist(gap_h, bins=30, alpha=0.7, color='green', edgecolor='black')
    plt.axvline(x=2*NOMINAL_GAP, color='red', linestyle='dashed', label="Nominal Gap (20 mm)")
    plt.xlabel("Gap in Height (mm)")
    plt.ylabel("Frequency")
    plt.title("Tolerance Analysis - Height Gap")
    plt.legend()

    plt.tight_layout()
    plt.show()
