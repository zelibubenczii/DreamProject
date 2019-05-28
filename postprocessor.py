import os, re, csv
dir = os.getcwd()

def read_node(s, idx = -1):
    """
    reads a given string s (x1, x2 ... xn) as an array
    returns array of x[i] for i in indices
    """
    
    ar = [eval(x) for x in re.sub('[\(\)]', "", s).split(" ")]
    
    if hasattr(idx, "__len__"):
        return [ar[i] for i in indices]
    elif idx < 0:
        return ar
    else:
        return ar[idx]


def parse_file(dir):
    """
    read the data file of openFoam (like U or Ux ...)
    return np.array of data
    """
    f = open(dir)
    content = f.readlines()

    for idx, line in enumerate(content):
        if re.match('\d+', line):
            length = eval(line)
        if re.match('\(', line):
            start = idx + 1
            break
            
    end = start + length
    
    xx = []
    for line in content[start:end]:
        xx.append(read_node(line, 0))
    if len(xx) == 1:
        return xx[0]
    else:
        return xx


def get_v_in(file_name):
    start = file_name.find('V_in=') + len('V_in=')
    return eval(file_name[start:])
    
subfolders = [f.path for f in os.scandir(dir) if (f.is_dir() and f.name != 'orig' and f.name.find('git') < 0) ]

output_file = open(dir + "/output.csv",'w')
output_writer = csv.writer(output_file)

input_file = open(dir + "/input.csv",'w')
input_writer = csv.writer(input_file)

for sf in subfolders:
    ux = parse_file(sf + '/0/Ux')
    uy = parse_file(sf + '/0/Uy')
    u = ux+uy
    output_writer.writerow(u)
    
    cx = parse_file(sf + '/0/Cx')
    cy = parse_file(sf + '/0/Cy')
    cc = cx + cy   
    
    v_in = get_v_in(sf)
    res = cc + [v_in]
    input_writer.writerow(res)

input_file.close()
output_file.close()
