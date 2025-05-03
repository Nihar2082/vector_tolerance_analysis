# 2D Vector-Based Tolerance Analysis with Monte Carlo Simulation and Machine Learning

This repository presents a comprehensive framework for simulating and optimizing manufacturing tolerances in 2D mechanical assemblies. Utilizing vector-based geometry, Monte Carlo simulations, and machine learning techniques, the project aims to identify and optimize Key Characteristics (KCs) that influence system variability.

## Overview

- The primary objective is to develop a 2D tolerance analysis model that:
- Implements a vector-based approach to analyze tolerance variations.
- Utilizes Python to create a simulation environment.
- Identifies the most relevant KCs affecting product performance.
- Conducts extensive Monte Carlo simulations with a large sample size.
- Analyzes the influence of tolerances on overall system variability.
- Trains an ML model to predict the most influential KCs based on input distributions.
- Optimizes the number of required measurements to reduce computation time while ensuring precision.

## Methodology

### 1. Vector-Based Tolerance Modeling
- Geometry Generation: Constructs a 2D representation of the tailgate-window system, incorporating rounded corners and defined gaps.

- Tolerance Definition: Establishes input distributions and tolerances based on real-world constraints.

### 2. Monte Carlo Simulation
- Sampling: Performs extensive simulations by randomly sampling input tolerances.

- Analysis: Evaluates the impact of these variations on the overall system, generating histograms and statistical data.

### 3. Machine Learning Integration
- KC Identification: Applies machine learning algorithms to determine the most influential KCs affecting system variability.

- Optimization: Reduces the number of required measurements while maintaining accuracy, thereby optimizing computational resources.

## 📁 Project Structure

vector_tolerance_analysis/
├── config.py              # Configuration settings for geometry, tolerances, and simulation parameters
├── geometry.py            # Functions to generate and manipulate 2D geometry
├── tolerance_analysis.py  # Monte Carlo simulation and statistical analysis
├── kc_identification.py   # Machine learning models for KC identification and optimization
├── main.py                # Main script to execute the entire analysis pipeline
├── tolerance_data.csv     # Sample input data for tolerances
├── output.png             # Visual representation of simulation results
├── push.bat               # Batch script for version control operations
└── README.md              # Project documentation

## Installation

### 1. Clone the Repository:
```
git clone https://github.com/Nihar2082/vector_tolerance_analysis.git
cd vector_tolerance_analysis
```
### 2. Create a Virtual Environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies:
```
pip install -r requirements.txt
```
Note: Ensure that requirements.txt is updated with all necessary packages.

## Usage

### 1. Configure Parameters:
- Modify config.py to set geometry parameters, tolerance ranges, and simulation settings.
### 2. Run the Analysis:
```
python main.py
```
This will execute the full pipeline: geometry generation, Monte Carlo simulation, KC identification, and result visualization.

### 3. View Results:

- Output statistics and plots will be saved in the project directory.
- output.png provides a visual summary of the simulation outcomes.

###  Sample Output
Include sample plots or statistical summaries here to illustrate the results.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

### License
This project is licensed under the MIT License. See the LICENSE file for details.


### Contact
For questions or suggestions, please contact nihar3010patel@gmail.com.

<!-- 
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
```
🔹 **matplotlib** → Used for visualizing simulation results with histograms and plots.  
🔹 **numpy** → Used for efficient numerical computations in the Monte Carlo simulation.  

### ✅ Step 3: Run the Analysis

**1️⃣ Open your terminal or PowerShell.**
**2️⃣ Navigate to your project folder:**

```bash
cd "F:\2. MASTER THESIS\vector_tolerance_analysis"
```
**3️⃣ Run the analysis:**

```bash
python main.py
```
**This executes the complete simulation, including geometry generation, Monte Carlo analysis, and Key Characteristics (KC) identification.**

### 📊 What You'll See

✅ Tailgate & Window Visualization:

- Displays the system with red zones highlighting the gap variations in the tailgate and window.

📈 Gap Variation Histograms:

- Visualizes the distribution of width and height variations in the gaps, allowing for analysis of how the gaps fluctuate across different runs.

🧠 Key Characteristic (KC) Contribution:

- Printed output showing the percent contribution of each Key Characteristic (KC) to the total variation.

Example:
- Tailgate contribution to gap variation: 79.40%  
- Window contribution to gap variation: 20.60%  



### 🧩 File Descriptions

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





 -->
