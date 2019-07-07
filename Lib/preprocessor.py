import os, re, sys
from shutil import copytree

from setRadius import *
from setVelocity import *
__all__ = ['setVelocity', 'setRadius']

def create_cases(root, args):
    R_0, dR, nR, V_0, dV, nV = [eval(ar) for ar in args[1:7]]
    # R_0, dR, nR, V_0, dV, nV = 0.6, 0.05, 3, 2, 0.5, 3

    for i in range(nR):
        R_i = R_0 + dR * i
        
        dir_Ri_V0 = "{}/R={}_V={}".format(root, round(R_i, 3), round(V_0, 3))
        if not os.path.exists(dir_Ri_V0):
            copytree(root+'/orig', dir_Ri_V0)
        else:
            print("WARNING! The directory {} already exists".format(dir_Ri_V0))
        set_radius(dir_Ri_V0, R_i)
        set_velocity(dir_Ri_V0, V_0)
        
        for j in range(i, nV):
            V_j = V_0 + dV * j
            
            dir_Ri_Vj = "{}/R={}_V={}".format(root, round(R_i, 3), round(V_j, 3))
            if not os.path.exists(dir_Ri_Vj):
                copytree(dir_Ri_V0, dir_Ri_Vj)
            else:
                print("WARNING! The directory {} already exists".format(dir_Ri_Vj))
            set_velocity(dir_Ri_Vj, V_j)

if __name__ == "__main__":
    root = os.getcwd()     
    create_cases(root, sys.argv)