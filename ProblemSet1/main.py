from ClassDef import Boson, Higgs
Boson = Boson("photon", 1, 50)
Boson.PrintInfo()

h = Higgs(momentum=100, MassMean=125)
h.PrintInfo()
print("Mass:", h.mass)
print("Energy:", h.Energy())

