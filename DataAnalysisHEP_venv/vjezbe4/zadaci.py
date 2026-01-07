import uproot
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import expon

def problem1():
    file = uproot.open('/home/public/data/Lifetime/Lifetime.root')
    tree = file[file.keys()[0]] 
    t = tree['t'].array()
    t = np.array(t)

    plt.figure(figsize=(8,6))
    plt.hist(t, bins=50, density=True, alpha=0.7)
    plt.xlabel("Lifetime")
    plt.ylabel("Probability density")
    plt.savefig("lifetime.jpg")
    plt.close()

def problem2():
    def exponential(t, tau):
        f = (tau**(-1))*np.exp(-t/tau)
        return f

    tau = [1,2,3,4]
    t = np.linspace(0, 10, 1000)
    y = [[],[],[],[]]
    for k in tau:
        for i in t:
            y[k-1].append(exponential(i,k))
        plt.plot(t,y[k-1], label=f"tau={k}")
    plt.legend()
    plt.savefig('theoreticalPDF.jpg')
    plt.close()

    tau = 2.0
    t = 1.0

    P = 1 - np.exp(-t/tau)
    print("Vjerojatnost:", P)

def problem3():
    tau = np.linspace(0.01, 5, 1000)
    t = 1.0

    L = (1/tau) * np.exp(-t/tau)

    plt.plot(tau, L)
    plt.xlabel(r'$\tau$ [s]')
    plt.ylabel(r'$\mathcal{L}(\tau)$')
    plt.savefig('fixed_t.jpg')
    plt.close()

def problem4():
    file = uproot.open('/home/public/data/Lifetime/Lifetime.root')
    tree = file[file.keys()[0]] 
    t = tree['t'].array()
    t = np.array(t)   
    N = len(t)
    S = np.sum(t)

    tau_vals = np.linspace(0.1, 5*np.mean(t), 1000)

    neg2lnL = 2*N*np.log(tau_vals) + 2*S/tau_vals

    plt.plot(tau_vals, neg2lnL)
    plt.xlabel(r'$\tau$')
    plt.ylabel(r'$-2\ln\mathcal{L}$')
    plt.savefig('log-likelihood.jpg')
    plt.close()

def problem5():
    file = uproot.open('/home/public/data/Lifetime/Lifetime.root')
    tree = file[file.keys()[0]] 
    t = tree['t'].array()
    t = np.array(t)
    loc, tau_hat = expon.fit(t, floc=0)
    N = len(t)
    sigma_tau = tau_hat / np.sqrt(N)

    print("tau (ML fit) =", tau_hat)
    print("uncertainty =", sigma_tau)