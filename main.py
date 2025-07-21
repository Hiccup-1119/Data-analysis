import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [200, 250, 300, 400]
}
df = pd.DataFrame(data)

print(df)
# Add a NumPy-calculated column (e.g., 10% bonus)
df['Bonus'] = np.array(df['Sales']) * 0.10

# Plot
plt.bar(df['Month'], df['Sales'], color='skyblue', label='Sales')
plt.plot(df['Month'], df['Bonus'], color='red', marker='o', label='Bonus')
plt.title('Monthly Sales and Bonus')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()
plt.show()