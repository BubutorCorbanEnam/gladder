import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def gladder(data, varname):
    """Replicates Stata's gladder function in Python by plotting histograms
    of various transformations to check normality."""

    # Replace inf values with NaN
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Handle missing or non-numeric values
    data = data.dropna(subset=[varname])
    if not np.issubdtype(data[varname].dtype, np.number):
        raise ValueError(f"The variable '{varname}' must be numeric.")

    transformations = {
        "Original": data[varname],
        "Log": np.log(data[varname] + 1),  # Adding 1 to avoid log(0)
        "Square Root": np.sqrt(data[varname]),
        "Inverse": 1 / (data[varname] + 1),  # Adding 1 to avoid division by zero
        "Square": data[varname] ** 2,
        "Cube Root": np.cbrt(data[varname]),
        "Inverse Square Root": 1 / (np.sqrt(data[varname]) + 1)
    }

    num_transformations = len(transformations)
    num_cols = 3
    num_rows = (num_transformations + num_cols - 1) // num_cols
    plt.figure(figsize=(12, 4 * num_rows))

    for i, (key, transformed_data) in enumerate(transformations.items(), 1):
        plt.subplot(num_rows, num_cols, i)
        sns.histplot(transformed_data, bins=30, kde=True)
        plt.title(key)

    plt.tight_layout()
    plt.show()
