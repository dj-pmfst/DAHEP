import numpy as np 
import matplotlib.pyplot as plt 
import math 

ac = np.array([9.8, 21.2, 34.5, 39.9, 48.5])
ac_er = np.array([1.0, 1.9, 3.1, 3.9, 5.1])
F = np.array([1,2,3,4,5])

w = 1/ac_er**2
m = np.sum(w*F**2)/np.sum(w*F*ac)
m_er = np.sqrt(1/np.sum(w*F**2))

F_fit = np.linspace(0,6,100)
a_fit = F_fit/m

plt.xlabel("F(N)")
plt.ylabel("a(m/s^2)")
plt.errorbar(F,ac, yerr=ac_er, fmt='o', label="data")
plt.plot(F_fit, a_fit, '-', label="fit")
plt.legend()
plt.savefig("fit_plot.png", dpi=300)   
plt.close() 

print("Vrijednost m i nesigurnost:",m, m_er)

def xi2():
    return np.sum((ac-theta*F)**2/(ac_er**2))


