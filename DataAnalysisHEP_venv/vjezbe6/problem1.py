import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm

N = 100
beta = np.linspace(0.1, 3, 5)  
mu = [0, 20, 50, 70, 100]
lamda = [1, 20, 35, 50, 70]
sigma = 5

for i in range(5):
    exp_sums = []
    gauss_sums = []
    poisson_sums = []

    for _ in range(10000):
        x = np.random.exponential(scale=beta[i], size=N)
        exp_sums.append(np.sum(x))

        g = np.random.normal(mu[i], sigma, size=N)
        gauss_sums.append(np.sum(g))

        p = np.random.poisson(lamda[i], size=N)
        poisson_sums.append(np.sum(p))
    
    exp_sums = np.array(exp_sums)

    mu_clt = exp_sums.mean()
    sigma_clt = exp_sums.std()

    x_plot = np.linspace(exp_sums.min(), exp_sums.max(), 1000)
    plt.hist(exp_sums, bins=50, density=True, alpha=0.3)
    plt.plot(x_plot, norm.pdf(x_plot, mu_clt, sigma_clt),
             label=f"β = {beta[i]:.2f}")

plt.xlabel("Sum")
plt.ylabel("Probability density")
plt.legend()
plt.savefig("clt.jpg")
plt.close()

