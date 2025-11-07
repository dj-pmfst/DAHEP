import numpy as np 

class Boson:
    isFermion=False
    def __init__(self):
        self.name = ''
        self.spin=0
        self.p=0
    def attributes(name, s, p):
        self.name=name
        self.spin=s
        self.p=p

    def PrintInfo():
        print('name=',{self.name}, 'spin=', {self.spin}, 'momentum=', {self.p})
    
    class Higgs:
        MassSigma=1
        def energy(m):
            MassMean=m 
            Mass=np.random.normal(MassMean, MassSigma)
            self.energy = np.sqrt(self.p^2 + Mass^2)
            return self.energy
