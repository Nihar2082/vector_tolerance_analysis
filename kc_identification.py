# kc_identification.py

import numpy as np
from config import *

def compute_variance_contributions():
    np.random.seed(42)
    tailgate_tol = np.random.normal(0, TAILGATE_TOL, NUM_SAMPLES)
    window_tol = np.random.normal(0, WINDOW_TOL, NUM_SAMPLES)

    var_tailgate = np.var(tailgate_tol)
    var_window = np.var(window_tol)

    total_var = var_tailgate + var_window

    tailgate_contrib = var_tailgate / total_var * 100
    window_contrib = var_window / total_var * 100

    return tailgate_contrib, window_contrib

# def plot_variance_contributions():
#     tailgate_contrib, window_contrib = compute_variance_contributions()

#     plt.figure(figsize=(8, 5))

