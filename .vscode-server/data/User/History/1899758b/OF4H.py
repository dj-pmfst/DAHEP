import uproot 
import numpy as np 
import matplotlib.pyplot as plt

file = uproot.open('/home/public/data/ggH125/ZZ4lAnalysis.root')

tree = file['ZZTree/candTree']
branches = tree.arrays()
pt = branches['LepPt']
eta = branches['LepEta']
phi = branches['LepPhi']

m = 0

def four_momentum(p, Eta, Phi):
    px = p * np.cos(Phi)
    py = p * np.sin(Phi)
    pz = p * np.sinh(Eta)
    E  = np.sqrt(px**2 + py**2 + pz**2)
    return px, py, pz, E

px, py, pz, E = four_momentum(pt, eta, phi)

E_z1  = E[:, 0]  + E[:, 1]
px_z1 = px[:, 0] + px[:, 1]
py_z1 = py[:, 0] + py[:, 1]
pz_z1 = pz[:, 0] + pz[:, 1]

m_z1 = np.sqrt(E_z1**2 - px_z1**2 - py_z1**2 - pz_z1**2)

E_z2  = E[:, 2]  + E[:, 3]
px_z2 = px[:, 2] + px[:, 3]
py_z2 = py[:, 2] + py[:, 3]
pz_z2 = pz[:, 2] + pz[:, 3]

m_z2 = np.sqrt(E_z2**2 - px_z2**2 - py_z2**2 - pz_z2**2)

E_h  = E[:, 0]  + E[:, 1] + E[:, 2]  + E[:, 3]
px_h = px[:, 0] + px[:, 1] + px[:, 2] + px[:, 3]
py_h = py[:, 0] + py[:, 1] + py[:, 2] + py[:, 3]
pz_h = pz[:, 0] + pz[:, 1] + pz[:, 2] + pz[:, 3]

m_h = np.sqrt(E_h**2 - px_h**2 - py_h**2 - pz_h**2)

plt.figure(figsize=(8, 6))


plt.hist(
    m_z1,
    bins=60,
    range=(60, 120),
    histtype='step',
    linewidth=2,
    color='blue',
    label='Z1 → ℓℓ'
)

plt.hist(
    m_z2,
    bins=60,
    range=(60, 120),
    histtype='step',
    linewidth=2,
    color='blue',
    label='Z2 → ℓℓ'
)

plt.hist(
    m_h,
    bins=60,
    range=(100, 150),
    histtype='step',
    linewidth=2,
    color='red',
    label='H → ZZ → 4ℓ'
)

plt.xlabel('Invariant Mass [GeV]')
plt.ylabel('Events')
plt.legend()
plt.tight_layout()
plt.savefig('leptopns-higgs-hist.png', dpi=300)
plt.close()
