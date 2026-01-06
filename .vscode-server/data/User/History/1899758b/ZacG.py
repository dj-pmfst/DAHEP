import uproot 
import numpy as np 

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

E_z1  = E[:, 0]  + E[:, 1]
px_z1 = px[:, 0] + px[:, 1]
py_z1 = py[:, 0] + py[:, 1]
pz_z1 = pz[:, 0] + pz[:, 1]

m_z1 = np.sqrt(E_z1**2 - px_z1**2 - py_z1**2 - pz_z1**2)

