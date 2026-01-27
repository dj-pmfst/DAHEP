import uproot
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.special import erfcinv

def problem1():
    mu = 165.5 
    sigma = 7.1
    N = 100
    n_experiments = 10**6

    test_heights = np.random.normal(mu, sigma, size=(n_experiments, N)).mean(axis=1)
    plt.hist(test_heights, bins=200, density=True, alpha=0.7)
    plt.xlabel("Sample mean height (cm)")
    plt.ylabel("Probability density")
    plt.savefig("test_statistic.jpg")
    plt.close()


    p = 0.05 
    file = uproot.open("/home/public/data/Height/Height.root")
    tree = file[file.keys()[0]]
    heights = tree.arrays(library="np")[list(tree.keys())[0]]
    x_bar_obs = np.mean(heights)
    p_value = np.mean(np.abs(test_heights - mu) >= abs(x_bar_obs - mu))
    z_score = np.sqrt(2) * erfcinv(2 * p_value)

    print(p_value, z_score)

    plt.hist(test_heights, bins=200, density=True, alpha=0.7)
    plt.axvline(x_bar_obs, color='red', linewidth=2, label="Observed mean")
    plt.xlabel("Sample mean height (cm)")
    plt.ylabel("Probability density")
    plt.legend()
    plt.savefig("observed.jpg")
    plt.close()


def problem2():
    N = 100
    n_experiments = 10**6

    countries = {
    "Spain": (168.0, 7.0),
    "France": (165.5, 7.1),
    "Italy": (166.1, 6.5),
    "Netherlands": (170.3, 7.5)
    }

    means = {}

    for name, (mu, sigma) in countries.items():
        samples = np.random.normal(mu, sigma, size=(n_experiments, N))
        means[name] = samples.mean(axis=1)

    file = uproot.open("/home/public/data/Height/Height.root")
    tree = file[file.keys()[0]]
    heights = tree.arrays(library="np")[list(tree.keys())[0]]
    x_obs = np.mean(heights)   

    for name, (mu, sigma) in countries.items():
        if (name != "Spain"):
            CL_A = 1 - np.mean(
            np.abs(means[name] - 168.0) <= abs(x_obs - 168.0)
            )
            print(name, CL_A)
    
    bins = np.linspace(162, 174, 300)
    plt.figure(figsize=(9, 6))

    plt.hist(means["Spain"], bins=bins, density=True,
            histtype="step", linewidth=2, label="Spain (H₀)")

    plt.hist(means["France"], bins=bins, density=True,
            histtype="step", linewidth=2, label="France")

    plt.hist(means["Italy"], bins=bins, density=True,
            histtype="step", linewidth=2, label="Italy")

    plt.hist(means["Netherlands"], bins=bins, density=True,
            histtype="step", linewidth=2, label="Netherlands")

    plt.axvline(x_obs, color="black", linestyle="--",
            linewidth=2, label="Measured mean")

    plt.xlabel("Mean height of 100 women (cm)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("h0_vs_h1s.jpg")
    plt.close()


problem2()