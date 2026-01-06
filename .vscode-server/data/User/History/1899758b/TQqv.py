import uproot 
import math

file = uproot.open('/home/public/data/ggH125/ZZ4lAnalysis.root')

tree = file['ZZTree/candTree']
branches = tree.arrays()
pt = branches['LepPt']
eta = branches['LepEta']
phi = branches['LepPhi']

m = 0

def p_x(p, Phi):
    return p*math.cos(Phi)
def p_y(p, Phi):
    return p*mat.sin(Phi)
def p_z(p, Eta):
    return p*mat.sinh(Eta)
def energy(x,y,z):
    E = math.sqrt(x)
