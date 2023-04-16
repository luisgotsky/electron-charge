import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]
y = [1.83, 1.8135, 1.772]
e = [0.01, 0.0104, 0.017]

t = np.linspace(1, 3, 1000)
z = [1.75882001076]*1000

plt.figure(figsize=(9, 6))
plt.errorbar(x, y, e, fmt="o", capsize=5, ecolor="black")
plt.xlabel("$Resultado$")
plt.ylabel("$\\frac{|e|}{m} * 10^{-11} (\\frac{C}{kg})$")
plt.plot(t, z, "--r", label="Valor teórico")
plt.legend(loc="upper right")
plt.grid()
plt.savefig("ResultsT.png", dpi=1200)