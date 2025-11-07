import numpy as np 

class Boson:
    isFermion=False
    def attributes(name, s, p):
        self.name=[name]
        self.spin=[s]
        self.p=[p]

    def PrintInfo():
        print('name=',{self.name[0]}, 'spin=', {self.spin[0]}, 'momentum=', {self.p[0]})
    
    class Higgs:
        MassSigma=1
        MassMean=1
        def energy():
            self.energy = np.sqrt()
