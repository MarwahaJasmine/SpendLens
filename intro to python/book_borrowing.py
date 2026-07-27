import matplotlib.pyplot as plt
import numpy as np

# 1. Fake data collected from the class (Happiness scale 1-10 vs Slices of Cheese)
cheese_slices = [1, 2, 3, 5, 0, 4, 2, 5, 1, 3]
happiness_score = [4, 5, 7, 9, 2, 8, 6, 10, 5, 7]

# 2. Create the scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(cheese_slices, happiness_score, color='gold', edgecolor='black', s=100, label='Students')

# 3. Add a fun trendline (Line of Best Fit)
m, b = np.polyfit(cheese_slices, happiness_score, 1)
plt.plot(cheese_slices, m * np.array(cheese_slices) + b, color='orange', linestyle='--', label='Cheese Power Trend')

# 4. Label the chart clearly for kids
plt.title("Does Eating More Cheese Make You Happier? 🧀", fontsize=14, fontweight='bold')
plt.xlabel("Slices of Cheese Consumed Per Day", fontsize=11)
plt.ylabel("Happiness Score (1 to 10)", fontsize=11)
plt.xlim(-0.5, 6)
plt.ylim(0, 11)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# 5. Show the plot
plt.show()