# # config.py

# NUM_SAMPLES = 1000
# TAILGATE_WIDTH = 1000  # mm
# TAILGATE_HEIGHT = 500  # mm
# WINDOW_WIDTH = 980     # mm
# WINDOW_HEIGHT = 480    # mm
# TAILGATE_TOL = 2       # mm
# WINDOW_TOL = 1         # mm
# NOMINAL_GAP = 10       # mm

# # Define the range of gap sizes to test
# GAP_MIN = 0.0           # Minimum gap size (mm)
# GAP_MAX = 10.0          # Maximum gap size (mm)
# GAP_STEP = 0.1          # Step size for gap (mm)


# config.py

NUM_SAMPLES = 1000
TAILGATE_WIDTH = 1000  # mm
TAILGATE_HEIGHT = 500  # mm
WINDOW_WIDTH = 999.8   # mm (just slightly smaller than tailgate width - 2 * 0.1)
WINDOW_HEIGHT = 499.8  # mm (slightly smaller than tailgate height - 2 * 0.1)
TAILGATE_TOL = 0.05    # mm (very small tolerance, realistic)
WINDOW_TOL = 0.05      # mm

NOMINAL_GAP = 0.1      # mm (small nominal gap)

# Define the range of gap sizes to test
GAP_MIN = 0.0          # Minimum gap size (mm)
GAP_MAX = 0.5          # Maximum gap size (mm)
GAP_STEP = 0.01        # Step size for gap (finer step for small gaps)
