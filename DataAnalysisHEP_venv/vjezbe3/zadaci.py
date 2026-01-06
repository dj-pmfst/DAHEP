import scipy 
from scipy.stats import norm
import numpy as np 
import matplotlib.pyplot as plt 

def problem1():       
    x = np.linspace(180, 220, 1000)

    params = [(205,2),(199,2),(203,2)]

    for i in range(len(params)):
        plt.plot(x, norm.pdf(x, params[i][0], params[i][1]), label=f"μ={params[i][0]}, σ={params[i][1]}")
    plt.xlabel('mass [GeV]')
    plt.ylabel('probability density')
    plt.legend()
    plt.savefig('gaussian.png')
    plt.close()

    mu = 200
    sigma = 2

    prob_205_up = 1 - norm.cdf(205, mu, sigma)

    prob_199_201 = norm.cdf(201, mu, sigma) - norm.cdf(199, mu, sigma)

    prob_203_up = 1 - norm.cdf(203, mu, sigma)
    prob_two_particles = prob_203_up ** 2 


def problem2():
    x = np.linspace(-5,5,1000)
    plt.plot(x, norm.cdf(x,0,1))
    plt.xlabel('x')
    plt.ylabel('CDF')
    plt.savefig('cdf.jpg')
    plt.close()


def acceptance_rejection(pdf, xmin, xmax, n):
    samples = []
    counter = 0
    pdf_max = max(pdf(np.linspace(xmin, xmax, 1000)))
    while (len(samples) <= n):
        x = np.random.uniform(xmin, xmax)
        y = np.random.uniform(0, pdf_max)
        counter += 1
        if y <= pdf(x):
            samples.append(x)
    return np.array(samples), counter

pdf = lambda x: norm.pdf(x, 0, 1)
samples, counter = acceptance_rejection(pdf, -5, 5, 10000)
print("Broj pokušaja:", counter)

plt.hist(samples, bins=50, density=True, alpha=0.7)
x = np.linspace(-5, 5, 1000)
plt.plot(x, pdf(x), 'r', lw=2)
plt.savefig('accepance-rejection.png')
plt.close()


n_samples = 10000
u = np.random.uniform(0,1,n_samples)
samples_inv = norm.ppf(u, 0, 1)  

plt.hist(samples_inv, bins=50, density=True, alpha=0.7)
plt.plot(x, norm.pdf(x, 0, 1))
x = np.linspace(-5, 5, 1000)
plt.savefig('inverse.png')
plt.xlabel("x")
plt.ylabel("Probability density")
plt.close()
