# **gladderstata**

gladderstata is a Python script that replicates Stata's gladder function by plotting histograms of various transformations to check for normality. This script includes error handling for non-numeric values and missing data, and dynamically adjusts the plot layout based on the number of transformations.

# Features
**Multiple Transformations**
The script applies a variety of transformations to the data, allowing users to explore different methods for achieving normality. The transformations include:

Original: The raw data without any transformation.

Log: Logarithmic transformation, useful for data with a skewed distribution.

Square Root: Square root transformation, often used for count data.

Inverse: Inverse transformation, which can be helpful for data with a heavy tail.

Square: Squaring the data, which can be useful for data with a left-skewed distribution.

Cube Root: Cube root transformation, providing a moderate adjustment to the data distribution.

Inverse Square Root: Inverse square root transformation, combining the effects of inverse and square root transformations.# Installation

To use this script, you'll need to have Python installed along with the following libraries:
numpy
matplotlib
seaborn
pandas

You can install these libraries using pip:
pip install numpy matplotlib seaborn pandas


# Usage
Import the Function: Ensure your script is named gladder_stata.py and import the gladder function.
from gladderstata import gladder

Prepare Your Data: Ensure your data is in a pandas DataFrame and the column you want to analyze is numeric.
import pandas as pd

# Example DataFrame
data = pd.DataFrame({
    'thalach': [150, 160, 170, 180, 190, 200, np.inf, -np.inf, np.nan]
})

Call the Function: Use the gladder function to plot the histograms.
gladder(data, 'thalach')

Example
Here's a complete example of how to use the gladder function:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from gladder_stata import gladder

# Example DataFrame
data = pd.DataFrame({
    'thalach': [150, 160, 170, 180, 190, 200, np.inf, -np.inf, np.nan]
})

# Replace inf values with NaN
data.replace([np.inf, -np.inf], np.nan, inplace=True)

# Call the gladder function
gladder(data, 'thalach')

