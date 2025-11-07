import classdef as cd 

a = cd.Boson()
a.attributes('Higgs', 0, 50)

a.PrintInfo()

b = a.Higgs()
print(b.energy(125))