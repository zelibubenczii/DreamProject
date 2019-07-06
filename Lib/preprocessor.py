import os, re, sys
from shutil import copytree

__all__ = ['setVelocity', 'setRadius']

if __name__ == "__main":
    R_0, dR, nR, V_0, dV, nV = sys.argv[1:7]
    root = os.getcwd()
    
    for i in range(nR):
        R_i = R_0 + dR * i
        
        dir_Ri_V0 = root + '/R={}_V={}'.format(R_i, V_0)
        if not os.path.exists(dir_Ri_V0):
            copytree(root+'/orig', dir_Ri_V0)
        else:
            print("WARNING! The directory {} already exists".format(dir_Ri_V0))
        set_radius(dir_Ri_V0, R_i)
        set_velocity(dir_Ri_V0, V_0)
        
        for j in range(i, nV):
            V_i = V0 + dV * i
            
            dir_Ri_Vi = dir + '/R={}_V={}'.format(R_i, V_i)
            if not os.path.exists(dir_Ri_V0):
                copytree(dir_Ri_V0, dir_Ri_Vi)
            else:
                print("WARNING! The directory {} already exists".format(dir_Ri_V0))
            set_velocity(dir_Ri_Vi, V_i)