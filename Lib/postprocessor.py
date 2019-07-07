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

def read_input(path):
    name = os.path.basename(path)
    R_s, V_in_s = name.split('_')
    R, V_in = re.search('(?<=\=)[\d.]+', R_s)[0], re.search('(?<=\=)[\d.]+', V_in_s)[0]
    return eval(R), eval(V_in)

if __name__ == "__main__":
    # dirs_to_discard = ['orig', '.git', 'Help', "Lib"]
    subfolders = [f.path for f in os.scandir(dir) if (f.is_dir() and f.name.find('R=') == 0 and f.name.find('_NN') < 0) ]
    file = open(dir + "/data.csv",'w')
    writer = csv.writer(file)

    for sf in subfolders:
        Ux, _ = read_data(sf + '/0/Ux')
        Uy, _ = read_data(sf + '/0/Uy')    
        Cx, _ = read_data(sf + '/0/Cx')
        Cy, _ = read_data(sf + '/0/Cy') 
        
        R, Vin = read_input(sf)

        for ux, uy, cx, cy in zip(Ux, Uy, Cx, Cy):
            row = [ux/Vin, uy/Vin, cx, cy, R, Vin]
            writer.writerow(row)
    file.close()


