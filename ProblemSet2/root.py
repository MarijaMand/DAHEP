import uproot
import math
import matplotlib.pyplot as plt

# vjezba
file = uproot.open('ggH125_ZZ4lAnalysis.root')

print(file.keys()) # daje popis imena objekata u dat
print(file.classnames()) # daje imena i što je to 

events = uproot.open('ggH125_ZZ4lAnalysis.root:ZZTree/candTree') # precac za stablo unutar datoteke, events je stablo
print(events)
print(events.typenames())
#

branches = events.arrays(["LepPt", "LepEta", "LepPhi"])

pt = branches['LepPt']
eta = branches['LepEta']
phi = branches['LepPhi']

print('Branch 1, Pt:')
print(pt)
print('Branch 2, Eta:')
print(eta)
print('Branch 3, Phi:')
print(phi)

# p_leptona = 0 
def inv_masa(pt, eta, phi):
    E = px = py = pz = 0
    for j in range(len(pt)): # za svaki lepton u skupini
        x = pt[j] * math.cos(phi[j])
        y = pt[j] * math.sin(phi[j])
        z = pt[j] * math.sinh(eta[j])
        px += x
        py += y
        pz += z
        E += math.sqrt(x**2 + y**2 + z**2)
    return math.sqrt(max(E**2 - px**2 - py**2 - pz**2, 0))

mase_Z1 = []
mase_H = []

for i in range(len(pt)): # za svaki dogadaj
    mase_Z1.append(inv_masa(pt[i][:2], eta[i][:2], phi[i][:2]))  # leptoni 1 i 2
    mase_H.append(inv_masa(pt[i], eta[i], phi[i]))   # sva 4 leptona

plt.hist(mase_H, bins=100, range=(0, 200), color="red", alpha=0.6, label="Higgs") #broj binova i range je x os
plt.hist(mase_Z1, bins=100, range=(0, 200), color="blue", alpha=0.6, label="Z1")
plt.xlabel("Invariant mass [GeV]")
plt.ylabel("Number of events")
plt.xlim(0, 200)                   
plt.ylim(bottom=0)                  
plt.margins(0)                     
plt.gca().set_facecolor("#e5e5e5")
plt.legend()
plt.show()