import classdef as cd 

a = cd.Boson('Higgs', 0, 50)
a.PrintInfo()
b = cd.Higgs
print(b.energy(125))