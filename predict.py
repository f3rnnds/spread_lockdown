import matplotlib.pyplot as plt
import numpy as np

N =        [20000, 40000, 80000, 160000]
ram =      [   14,    55,   219,    875]
duration = [   30,    87,   408,   2077]
data =     [   12,    33,    98,    331]

def polyfit(y):
    c = np.polyfit(range(len(y)), y, 2)
    p = np.poly1d(c)
    fit = p(len(y) + 1)
    return fit

fig, axs = plt.subplots(2, 2, sharex=True)

axs[0, 0].set_title("N")
axs[0, 0].plot(N)

axs[0, 1].set_title(f"RAM, predicted={polyfit(ram)}")
axs[0, 1].plot(ram, "tab:orange")

axs[1, 0].set_title(f"duration (s), predicted={polyfit(ram)}")
axs[1, 0].plot(duration, "tab:green")

axs[1, 1].set_title(f"data (MB), predicted={polyfit(data)}")
axs[1, 1].plot(data, "tab:red")

plt.show()