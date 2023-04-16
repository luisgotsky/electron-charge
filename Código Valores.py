import matplotlib.pyplot as plt

x = [124, 138, 196, 185, 158]
y = [2.23, 1.99, 1.772, 1.808, 1.865]
e = [0.07, 0.04, 0.017, 0.019, 0.018]

plt.figure(figsize=(9, 6))
plt.errorbar(x, y, e, fmt="o", capsize=5, ecolor="black")
plt.xlabel("$\\Delta U (V)$")
plt.ylabel("$\\frac{|e|}{m} * 10^{-11} (\\frac{C}{kg})$")
plt.grid()
plt.savefig("Values.png", dpi=1200)

p = [1/i**2 for i in e]
mediaPond = 0

for i in range(len(y)):
    
    mediaPond += y[i]*p[i]
    
print(mediaPond/sum(p))
err = (1/sum(p))**0.5
print(err)

mediaPond2 = 0

for i in range(2, len(y)):
    
    mediaPond2 += y[i]*p[i]
    
print(mediaPond2/sum(p[2::]))
err2 = (1/sum(p[2::]))**0.5
print(err2)

plt.figure(figsize=(9, 6))
plt.errorbar(x[2::], y[2::], e[2::], fmt="o", capsize=5, ecolor="black")
plt.xlabel("$\\Delta U (V)$")
plt.ylabel("$\\frac{|e|}{m} * 10^{-11} (\\frac{C}{kg})$")
plt.grid()
plt.savefig("Values2.png", dpi=1200)