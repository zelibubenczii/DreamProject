import os, re, csv, fileinput, sys
from postprocessor import read_data

case_path = 'C:/Program Files/blueCFD-Core-2017/ofuser-of5/run/check/V_in=1.0_NN'

def set_U_i(dir, x_i):
    """
    takes the data (represented as a list of strings, i.e. a part of an opeanFoam file,
    and changes the corresponding values in each string)
    """
    x_i = x_i.lower()
    
    with open(dir+'/_CSV/U'+x_i+'.csv', 'r') as f:
        reader = csv.reader(f)
        U_new = list(reader)[0]
    
    print("DIR:", dir + '/0/U' + x_i)
    print("U_x.size = ", len(U_new)) 
    _, start = read_data(dir + '/0/U' + x_i)
    
    U_file_path = dir + '/0/U' + x_i
    for idx, line in enumerate(fileinput.input(U_file_path, inplace='True')):     
        if idx >= start and idx - start < len(U_new):
            line = U_new[idx-start]
        print(line.rstrip())
set_U_i(case_path, 'x')