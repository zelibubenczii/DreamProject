import os, re, csv
dir = os.getcwd()
# dir = os.path.dirname(path)

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


def read_data(dir):
    """
    read the data file of openFoam (like U or Ux ...),
    seeks for the area, corresponded to the values of the parameter at each control volume and
    returns it as a list of strings
    
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
    
    return xx, start

def get_v_in(file_name):
    start = file_name.find('V_in=') + len('V_in=')
    return eval(file_name[start:])

if __name__ == "__main__":
    dirs_to_discard = ['orig', '.git', 'Help', "Lib"]
    subfolders = [f.path for f in os.scandir(dir) if (f.is_dir() and f.name not in dirs_to_discard and f.name.find('_NN') < 0) ]
    file = open(dir + "/data.csv",'w')
    writer = csv.writer(file)

    for sf in subfolders:
        Ux = read_data(sf + '/0/Ux')
        Uy = read_data(sf + '/0/Uy')    
        Cx = read_data(sf + '/0/Cx')
        Cy = read_data(sf + '/0/Cy') 
        
        v_in = get_v_in(sf)

        for ux, uy, cx, cy in zip(Ux, Uy, Cx, Cy):
            # row = [ux/v_in, uy/v_in, cx, cy, v_in]
            row = [ux, uy, cx, cy, v_in]
            writer.writerow(row)

    file.close()

