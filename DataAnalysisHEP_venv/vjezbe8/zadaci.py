import numpy as np 
import math 
from math import factorial as f
import matplotlib.pyplot as plt 

def binomial(r, p, N):
    B = (f(N)/(f(r)*f(N-r)))*(p**(r))*(1-p)**(N-r)
    return B


def lower_tail(r, p, N):
    return sum(binomial(k, p, N) for k in range(0, r + 1))

def upper_tail(r, p, N):
    return sum(binomial(k, p, N) for k in range(r, N + 1))


def cp_lower(r, N, CL):
    alpha = 1 - CL
    p = 0.0
    while p <= 1.0:
        if upper_tail(r, p, N) >= alpha:
            return p
        p += 0.001
    return 1.0

def cp_upper(r, N, CL):
    alpha = 1 - CL
    p = 1.0
    while p >= 0.0:
        if lower_tail(r, p, N) >= alpha:
            return p
        p -= 0.001
    return 0.0


def clopper_pearson(r, N, CL):
    lower = cp_lower(r, N, CL)
    upper = cp_upper(r, N, CL)
    return lower, upper

def cl_results():
    CL_1sigma = 0.6827
    N = 10

    print("1σ Clopper–Pearson intervals for N = 10:\n")

    for r in range(0, N + 1):
        p_low, p_up = clopper_pearson(r, N, CL_1sigma)
        print(f"r = {r:2d} : p ∈ [{p_low:.3f}, {p_up:.3f}]")


def neyman(p, N, CL):
    probs = []

    for r in range(N + 1):
        value = binomial(r, p, N)
        probs.append((r, value))

    probs.sort(key=lambda x: x[1], reverse=True)

    accepted = []
    total = 0.0

    for r, pr in probs:
        accepted.append(r)
        total += pr
        if total >= CL:
            break

    return sorted(accepted)


def neyman_plot(N=10, CL=0.6827):
    p_values = np.linspace(0, 1, 1001)

    belt = {r: [] for r in range(N + 1)}

    for p in p_values:
        accepted_r = neyman(p, N, CL)
        for r in accepted_r:
            belt[r].append(p)

    plt.figure(figsize=(8, 6))

    for r in range(N + 1):
        if belt[r]:
            plt.hlines(
                y=r,
                xmin=min(belt[r]),
                xmax=max(belt[r]),
                linewidth=2
            )

    plt.xlabel("True success probability p")
    plt.ylabel("Number of successes r")
    plt.title("1σ Neyman Confidence Belt (N = 10)")
    plt.grid(True)
    plt.savefig("neyman.jpg")
    plt.close()


neyman_plot(N=10, CL=0.6827)

N = 10
CL = 0.6827
p_true = 1/6
n_experiments = 1000

covered = 0

for _ in range(n_experiments):
    rolls = np.random.randint(1, 7, size=N)
    r = np.sum(rolls == 6)

    p_low, p_up = clopper_pearson(r, N, CL)

    if p_low <= p_true <= p_up:
        covered += 1

print(f"Covered {covered} out of {n_experiments} experiments")
print(f"Coverage = {covered / n_experiments:.3f}")