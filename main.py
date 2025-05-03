# ===========================
# main.py (Updated Version)
# ===========================

from geometry import select_and_measure_gap
from tolerance_analysis import simulate_tolerances, plot_gap_histograms
from kc_identification import compute_variance_contributions

# Step 1: Simulate tolerances and gaps
gap_w, gap_h = simulate_tolerances()

# Step 2: Plot histogram of gap distribution
plot_gap_histograms(gap_w, gap_h)

# Step 3: Identify Key Characteristics
kc1, kc2 = compute_variance_contributions()
print(f"Tailgate contribution to gap variation: {kc1:.2f}%")
print(f"Window contribution to gap variation: {kc2:.2f}%")

# Step 4: Interactive Geometry + Gap Measurement
# One plot only — with selection and gap shown
select_and_measure_gap()
