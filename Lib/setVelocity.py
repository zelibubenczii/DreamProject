import re

def set_velocity(dir, V_in_new):
    #this dictionary will be used as a map to create new inputs
    var_lines = {'U' : {'relative_path' : "/0/U"}}
    
    var_lines = get_var_lines(dir, var_lines)
    
    line_0 = var_lines['U']['value']
    line_new, u = change_line_U(line_0, V_in_new)
    
    U_path = dir + var_lines['U']['relative_path']
    replace_line_in_file(U_path, line_new, var_lines['U']['idx'])

def get_var_lines(dir, var_lines):
    """
    looks up in input files and fills var_lines dictionary
    """    
    #read file as an array of lines
    file_path = dir + '/0/U'
    file_lines = open(file_path, 'r').readlines()
    
    #now - just to fine a line with the part "constant" and take out the part (..., ..., ...) as an output
    for idx, line in enumerate(file_lines):
        if line.find('constant (') > 0:
            line_idx = idx
            value_0 = line
            break
            
    var_lines['U']['idx'] = line_idx
    var_lines['U']['value'] = value_0
    
    return var_lines

def change_line_U(line, u):
    """
    U_0 = [u0, v0, w0]
    delta_U = [du, dv, dw]
    input: line, sort of "uniformValue    constant (u v w);", where u, v, w - some numbers
    output: "uniformValue    constant (u+n*du v+n*dv w+n*dw);"
    """
    #this line finds and parses a part of the line to array, i.e. '(1, 0, 0)' => [1, 0, 0]
    # value_0 = [eval(x) for x in re.search('(\d |\d)+', line).group().split(" ")]
    value_new = [u, 0, 0]
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

