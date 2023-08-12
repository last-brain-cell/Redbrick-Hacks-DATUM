# import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import find_peaks


data = pd.read_csv("../frontend/blood_oxygen_data.csv", skiprows=1, names=['timestamp', 'blood_oxygen'])
timestamp = data['timestamp']
blood_oxygen = data['blood_oxygen']

plt.figure(figsize=(8, 4))
plt.plot(timestamp, blood_oxygen, color='green', linewidth=1.5)  # Use green color for blood oxygen

plt.title("Blood Oxygen Monitor")  # Update the title
plt.xlabel("Time")
plt.ylabel("Blood Oxygen Level")  # Update the y-axis label

plt.grid(True, linestyle='--', alpha=0.7)

# Horizontal line representing average blood oxygen level
average_blood_oxygen = np.mean(blood_oxygen)
plt.axhline(y=average_blood_oxygen, color='blue', linestyle=':', label='Average Blood Oxygen')

# Highlighting the troughs and peaks
peaks, _ = find_peaks(blood_oxygen, height=0.5)
plt.plot(timestamp[peaks], blood_oxygen[peaks], 'ro', markersize=5, label='Oxygen Peaks')  # Use red color for peaks

plt.legend()
plt.tight_layout()
plt.show()
