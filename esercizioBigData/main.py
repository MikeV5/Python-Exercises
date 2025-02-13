# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import numpy as np
import matplotlib.pyplot as plt

# Data for Producer A
data_a = np.array([
    [2, 85],
    [1, 80],
    [2, 70],
    [1, 60],
    [1, 55],
    [1, 50],
    [2, 40],
    [2, 30],
    [2, 20],
    [1, 10]
])

# Data for Producer B
data_b = np.array([
    [14, 50],
    [1, 49]
])

# Calculate mean and standard deviation for each producer
mean_a, std_a = np.mean(data_a[:, 1]), np.std(data_a[:, 1])
mean_b, std_b = np.mean(data_b[:, 1]), np.std(data_b[:, 1])

print("Producer A - Mean: {:.2f}, Standard Deviation: {:.2f}".format(mean_a, std_a))
print("Producer B - Mean: {:.2f}, Standard Deviation: {:.2f}".format(mean_b, std_b))

# Calculate probability density function for normal distribution
x = np.linspace(0, 100, 1000)
pdf_a = 1/(std_a * np.sqrt(2*np.pi)) * np.exp(-np.power(x-mean_a, 2)/(2*np.power(std_a, 2)))
pdf_b = 1/(std_b * np.sqrt(2*np.pi)) * np.exp(-np.power(x-mean_b, 2)/(2*np.power(std_b, 2)))

# Plot probability density function
plt.plot(x, pdf_a, label="Producer A")
plt.plot(x, pdf_b, label="Producer B")
plt.legend()
plt.xlabel("Battery Life (months)")
plt.ylabel("Probability Density")
plt.show()