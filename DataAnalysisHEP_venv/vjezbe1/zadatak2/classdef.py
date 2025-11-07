import numpy as np 

class Boson:
    def __init__(self,name, s, p):
        self.isFermion=False
        self.name=name
        self.spin=s
        self.p=p

    def PrintInfo(self):
        print('name=',{self.name}, 'spin=', {self.spin}, 'momentum=', {self.p})
    
class Higgs(Boson):
    def __init__(self,name,s,p):
        Boson.__init__(self,name,s,p)
        self.MassSigma=1
    def energy(self,m):
        MassMean=m 
        Mass=np.random.normal(MassMean, self.MassSigma)
        self.energy = np.sqrt(self.p**2 + Mass**2)
        return self.energy
