import numpy as np 

class Boson:
    def __init__(self):
        self.isFermion=False

    def attributes(self,name, s, p):


    def PrintInfo(self):
        print('name=',{self.name}, 'spin=', {self.spin}, 'momentum=', {self.p})
    
    class Higgs:
        def __init__(self):
            self.MassSigma=1
        def energy(self,m):
            MassMean=m 
            Mass=np.random.normal(MassMean, self.MassSigma)
            self.energy = np.sqrt(self.p^2 + Mass^2)
            return self.energy
