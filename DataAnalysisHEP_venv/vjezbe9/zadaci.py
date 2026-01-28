import numpy as np 
import matplotlib.pyplot as plt 
import uproot
from scipy.stats import chi2


n_experiments = 1000
N = 1000
mu = 5 
sigma = 2

q_values = []

for e in range (n_experiments):
    x = np.random.normal(mu, sigma, N)

    mu_hat = np.mean(x)
    sigma_hat = np.std(x, ddof=0)

    ll_H0 = (
        -N * np.log(sigma_hat)
        - np.sum((x - mu)**2) / (2 * sigma_hat**2)
    )

    ll_H1 = (
        -N * np.log(sigma_hat)
        - np.sum((x - mu_hat)**2) / (2 * sigma_hat**2)
    )

    q = -2 * (ll_H0 - ll_H1)
    q_values.append(q)

q_values = np.array(q_values)


plt.figure(figsize=(8, 6))
plt.hist(q_values, bins=50, density=True, alpha=0.6, label="Monte Carlo")

x = np.linspace(0, 10, 500)
plt.plot(x, chi2.pdf(x, df=1), 'r-', lw=2, label=r"$\chi^2_1$")

plt.xlabel(r"$-2 \ln \lambda$")
plt.ylabel("Probability density")
plt.legend()
plt.savefig("wilks.jpg")
plt.close()


x = np.linspace(0, 20, 1000)

plt.figure(figsize=(8, 6))

for k in range(1, 6):
    plt.plot(x, chi2.cdf(x, df=k), label=f"k = {k}")

plt.xlabel("x")
plt.ylabel("CDF")
plt.legend()
plt.savefig("cdf.jpg")
plt.close()



file = uproot.open("/home/public/data/GaussData.root")

tree = file[file.keys()[0]]
x = tree.arrays(library="np")[tree.keys()[0]]

N = len(x)
mu_hat = np.mean(x)
sigma_hat = np.std(x, ddof=0)

def log_likelihood(mu, data, sigma):
    return -np.sum((data - mu)**2) / (2 * sigma**2)


delta_mu = 5 * sigma_hat / np.sqrt(N)

mu_values = np.linspace(mu_hat - delta_mu,
                         mu_hat + delta_mu, 500)


mu_hat = np.mean(x)
sigma_hat = np.std(x, ddof=0)

ll_max = log_likelihood(mu_hat, x, sigma_hat)

q_values = []
for mu in mu_values:
    ll = log_likelihood(mu, x, sigma_hat)
    q_values.append(-2 * (ll - ll_max))

q_values = np.array(q_values)
inside = q_values <= 4

mu_lower = mu_values[inside][0]
mu_upper = mu_values[inside][-1]

print(f"95.4% CL interval: [{mu_lower:.3f}, {mu_upper:.3f}]")

plt.figure(figsize=(8, 6))

plt.plot(mu_values, q_values, label=r"$-2\Delta\ln L(\mu)$")
plt.axhline(4, color="red", linestyle="--",
            label=r"$\chi^2_1 = 3.98$")

plt.axvline(mu_lower, color="black", linestyle=":")
plt.axvline(mu_upper, color="black", linestyle=":")

plt.ylim(0, 5)
plt.xlabel(r"$\mu$")
plt.ylabel(r"$-2\Delta\ln L$")
plt.legend()
plt.savefig("likelihood.jpg")
plt.close()
