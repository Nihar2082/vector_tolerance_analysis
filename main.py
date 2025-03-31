# main.py

from geometry import draw_geometry_with_gap
from tolerance_analysis import simulate_tolerances, plot_gap_histograms
from kc_identification import compute_variance_contributions

# Step 1: Draw nominal geometry
draw_geometry_with_gap()

# Step 2: Simulate tolerances and gaps
gap_w, gap_h = simulate_tolerances()

# Step 3: Plot histogram of gap distribution
plot_gap_histograms(gap_w, gap_h)

# Step 4: Identify Key Characteristics
kc1, kc2 = compute_variance_contributions()
print(f"Tailgate contribution to gap variation: {kc1:.2f}%")
print(f"Window contribution to gap variation: {kc2:.2f}%")
