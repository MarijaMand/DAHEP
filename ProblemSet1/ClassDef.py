import numpy as np
import matplotlib.pyplot as plt

class Boson:
    isFermion = False
    def __init__(self, name, spin, momentum):
        self.name = name 
        self.spin = spin
        self.momentum = momentum 
    
    def PrintInfo(self):
        print(self.name)
        print(self.spin)
        print(self.momentum)
        print('Fermion: ', self.isFermion)

class Higgs(Boson):
    MassSigma = 1
    def __init__(self, momentum, MassMean = 125):
        super().__init__("Higgs", 0, momentum)
        self.MassMean = MassMean
        self.mass = np.random.normal(self.MassMean, self.MassSigma)
    
    def Energy(self):
        energy = np.sqrt(self.momentum**2 + self.mass**2)
        return energy