import numpy as np 
import matplotlib.pyplot as plt 
import math 
from scipy.interpolate import interp1d

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

def xi2(t):
    return np.sum((ac-t*F)**2/(ac_er**2))

theta = np.linspace(0,11,100)
xi = np.array([xi2(i) for i in theta])

plt.xlabel("theta")
plt.ylabel("Xi^2")
plt.plot(theta, xi)
plt.savefig("xi_plot.png", dpi=300)
plt.close()

theta_hat = theta[np.argmin(xi)] 

xi2 = xi - (np.min(xi) + 1)

level = np.min(xi) + 1

i_left = np.where(theta < theta_hat)[0]
theta_minus = np.interp(
    level,
    xi[i_left][::-1],
    theta[i_left][::-1]
)

i_right = np.where(theta > theta_hat)[0]
theta_plus = np.interp(
    level,
    xi[i_right],
    theta[i_right]
)


thera_er = (theta_plus-theta_minus)/2

plt.xlabel("theta")
plt.ylabel("Xi^2")
plt.ylim(0,12)
plt.xlim(8,12)
plt.plot(theta, xi)

plt.axhline(np.min(xi), linestyle='--', color='red')
plt.axhline(np.min(xi) + 1, linestyle='--', color='red')

plt.axvline(theta_hat, linestyle='--', color='red')
plt.axvline(theta_minus, linestyle='--', color='red')
plt.axvline(theta_plus, linestyle='--', color='red')

plt.savefig("xi_plot_dashed.png", dpi=300)
plt.close()