import uproot 
import math

file = uproot.open('/home/public/data/ggH125/ZZ4lAnalysis.root')

tree = file['ZZTree/candTree']
branches = tree.arrays()
pt = branches['LepPt']
eta = branches['LepEta']
phi = branches['LepPhi']

m = 0

def four_momentum(p, Eta, Phi):
    px = pt * np.cos(Phi)
    py = pt * np.sin(Phi)
    pz = pt * np.sinh(Eta)
    E  = np.sqrt(px**2 + py**2 + pz**2)
    return px, py, pz, E

px, py, pz, E = four_momentum(pt, eta, phi)

p_z1 = math.sqrt()
