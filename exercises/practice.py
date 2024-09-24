import numpy as np

# Define the sample points
x = np.linspace(0, 1, 11)

# Define the function and polynomial approximations
f_x = np.sin(x)
P0_x = np.ones_like(x)
P9_x = x**9

# Calculate the errors
error_P0 = np.sqrt(np.sum((f_x - P0_x) ** 2))
error_P9 = np.sqrt(np.sum((f_x - P9_x) ** 2))

print(f"Error for P0(x) = 1: {error_P0}")
print(f"Error for P9(x) = x^9: {error_P9}")
