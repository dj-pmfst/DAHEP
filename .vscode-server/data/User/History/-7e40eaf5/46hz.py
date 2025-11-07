import classdef as cd 

a = cd.Boson('Higgs', 0, 50)
a.PrintInfo()

b = a.Higgs()
print(b.energy(125))