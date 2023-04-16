import matplotlib.pyplot as plt
import numpy as np
import xlrd as xc

wb = xc.open_workbook("E2.xls")

for i in range(1, 6):
    
    sh = wb.sheet_by_index(i)
    x, y, e = [], [], []
    
    for j in range(4):
        
        x.append(sh.cell_value(j+1, 4))
        y.append(sh.cell_value(j+1, 5))
        e.append(sh.cell_value(j+8, 4))

    t = np.linspace(x[0], x[3])
    lin = np.polyfit(x, y, 1)
    a, b = round(lin[0]/1E11, 2), round(lin[1]/1E7, 2)
    V, R2 = sh.cell_value(1, 2), round(sh.cell_value(9, 1), 4)
    
    plt.figure(figsize=(9, 6))
    plt.errorbar(x, y, yerr=e ,fmt="o", ecolor="black", capsize=5)
    plt.title(str(V) + "V")
    plt.grid()
    plt.plot(t, np.polyval(lin, t), "r--")
    plt.text(x[1], y[3], "$y = $" + str(a) +
             "$*10^{11}x $" + str(b) + "$*10^{7}$ \n $R^{2} = $" + str(R2), 
             horizontalalignment = "center")
    plt.xlabel("$r^{2} (m^{2})$")
    plt.ylabel("$(\\frac{5}{4})^{3} \\ \\frac{2 \\ R^{2} \\Delta U}{\\mu_{0}^{2} \\ N^{2} \\ I^{2}}$")
    plt.savefig(str(V) + "V.png", dpi=1200)