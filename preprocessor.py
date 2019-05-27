import os, re
# from distutils.dir_util import copy_tree
from shutil import copytree


#this dictionary will be used as a map to create new inputs
var_lines = {'U' : {'relative_path' : "/0/U"}}

def get_var_lines(dir_path):
    """
    looks up in input files and fills var_lines dictionary
    """    
    #read file as an array of lines
    file_path = dir_path + '/orig/0/U'
    file_lines = open(file_path, 'r').readlines()
    
    #now - just to fine a line with the part "constant" and take out the part (..., ..., ...) as an output
    for idx, line in enumerate(file_lines):
        if line.find('constant (') > 0:
            line_idx = idx
            value_0 = line
            break
#             value0 = re.search('(\d |\d)+', line).group()            
    var_lines['U']['idx'] = line_idx
    var_lines['U']['value'] = value_0

def create_cases(dir, delta={"U":[0.1, 0, 0]}, N=3):
    """
    delta = {"U": [dU, dV, dW], ....}
    creates folders with new cases increasing iteratevly all variables (var_lines.keys()) in N steps
    """
    for i in range(N):
        line_0 = var_lines['U']['value']
        line_new, u = change_line_U(line_0, delta['U'], i)
        dir_new = dir + '/V_in=' + str(u)
#         os.makedirs(filepath_new)
        if not os.path.exists(dir_new):
            copytree(dir+'/orig', dir_new)
        else:
            print("WARNING! The directory {} already exists".format(dir_new))
        
        U_path = dir_new + var_lines['U']['relative_path']
        replace_line_in_file(U_path, line_new, var_lines['U']['idx'])


def change_line_U(line, delta_U, n):
    """
    delta_U = (du, dv, dw)
    input: line, sort of "uniformValue    constant (u v w);", where u, v, w - some numbers
    output: "uniformValue    constant (u+n*du v+n*dv w+n*dw);"
    """
    #this line finds and parses a part of the line to array, i.e. '(1, 0, 0)' => [1, 0, 0]
    value_0 = [eval(x) for x in re.search('(\d |\d)+', line).group().split(" ")]
    value_new = [x + n * y for x, y in zip(value_0, delta_U)]
    value_new_str = '('+ " ".join(str(x) for x in value_new) + ')'
    line_new = re.sub('\([\d ]+\)', value_new_str, line)
    return line_new, value_new[0]

def replace_line_in_file(file_path, new_line, id_line):
    """
    replaces the line number = id_line in the given file to new_line
    """
    f = open(file_path, 'r')
    content = f.readlines()
    content[id_line] = new_line
    f.close()
    
    f = open(file_path, 'w')
    for line in content:
            f.write(line)
    f.close()
    

dir = os.getcwd()
get_var_lines(dir)
create_cases(dir)