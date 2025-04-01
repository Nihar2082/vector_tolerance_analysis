# 📐 2D Vector-Based Tolerance Analysis with Monte Carlo Simulation

This project simulates manufacturing variations in a tailgate-window system using **vector-based geometry** and **Monte Carlo tolerance analysis** in Python. It also identifies **Key Characteristics (KCs)** affecting system variation.

## 📁 Project Structure

vector_tolerance_analysis/  
│── config.py              # Centralized settings for geometry, tolerances, and sample count  
│── geometry.py            # Generates tailgate & window geometry with gaps (rounded corners)  
│── tolerance_analysis.py  # Performs Monte Carlo simulation and creates gap histograms  
│── kc_identification.py   # Identifies Key Characteristics (KCs) by analyzing variance  
└── main.py                # Orchestrates all modules and runs the complete analysis  


## 🚀 How to Run

### ✅ Step 1: Check if Python is Installed  
Most systems already have Python installed. To check, open a terminal or command prompt and run:  

```sh
python --version
```

### ✅ Step 2: Install Required Libraries

Open your terminal or PowerShell and run:

```bash
python -m pip install matplotlib numpy
✅ Step 3: Run the Analysis
Navigate to your project folder and run:

bash
Copy
Edit
python main.py
📊 What You'll See
📐 Tailgate and window visualization with red zones for visual gaps.

📈 Histograms showing the variation in width and height gaps.

🧠 Printed output showing Key Characteristic contribution, like:

pgsql
Copy
Edit
Tailgate contribution to gap variation: 65.80%
Window contribution to gap variation: 34.20%
🧩 File Descriptions
📁 config.py – The Settings File
Purpose: Stores all your important parameters in one place.

🔧 Contains:

Nominal dimensions (tailgate & window)

Tolerance values

Number of Monte Carlo samples

Gap size

🧠 Why it’s helpful: You only need to change numbers once here, and the whole system uses the new values.

📁 geometry.py – The Drawing Artist
Purpose: Visually draws the tailgate and window with gaps and rounded corners.

🎨 What it does:

Draws a rectangle for the tailgate

Draws a smaller rectangle (inset) for the window

Shades the gap between them using red zones

Adds labels like "Left Gap", "Top Gap", etc.

🔎 Uses: matplotlib.patches for custom shapes

📁 tolerance_analysis.py – The Simulator
Purpose: Runs the Monte Carlo simulation to simulate real-world variation.

🧮 What it does:

Randomly generates size variations (based on normal distribution)

Calculates the gap in width and height

Plots histograms to show how much variation happens

📊 Visual Output:

Histogram of width gaps

Histogram of height gaps

📁 kc_identification.py – The KC Detector
Purpose: Identifies which dimension (tailgate or window) is more responsible for variation.

🧠 What it does:

Uses variance analysis to compute how much each component contributes to gap variation

Returns results like:

matlab
Copy
Edit
Tailgate contributes 65.8%
Window contributes 34.2%
🎯 Helps prioritize which part’s tolerance to control more tightly.

📁 main.py – The Conductor
Purpose: Runs everything in the right order like a project manager.

🎯 What it does:

Draws the geometry

Simulates the tolerances

Shows histograms of gap variations

Prints Key Characteristic contributions

📌 You just run this one file to trigger the full analysis pipeline.

✅ Next Steps (Optional Ideas)
Add ML module to predict which tolerances are most influential

Animate the gap variation across samples

Export results to CSV/Excel for reports

📬 Questions or Help?
Feel free to open an issue or message if you want help expanding this into Machine Learning, animation, or 3D!

vbnet
Copy
Edit

Let me know if you'd like me to include example output images, or turn this into a GitHub-style project with `.gitignore`, sample data folder, etc.






