import math, re, fileinput

def set_radius(dir, R_new):
    file_path = dir + '/system/blockMeshDict'
    with open(file_path, 'r') as f:
        file_lines = f.readlines()

    points_to_scale = find_cylinder_points(file_lines)
    file_lines = change_point_lines(file_lines, points_to_scale, R_new)
    file_lines = change_arc_lines(file_lines, R_new)

    with open(file_path, 'w') as file:
        for line in file_lines:
            file.write(line)     

def change_point_lines(file_lines, points_to_scale, R_new):
    #to do in future: write a func to find n_points
    n_points = 19
    
    for idx, line in enumerate(file_lines):
        if line.find('points[')>=0:
            start = idx
            break
            
    idx_to_scale = [p + start for p in points_to_scale]
    for i in idx_to_scale:
        file_lines[i] = scale_point_inline(file_lines[i], R_new)
    
    scale_upper_points(file_lines, start)
    scale_side_points(file_lines, start)

    return file_lines

def find_cylinder_points(file_lines):
    n_points = 19
    s_points = ""
    
    for line in file_lines:
        if line.find('arc')>=0:
            s = re.search('(?<=c)[\d\ ]+(?=\()', line)[0]
            s_points += s
            
    points = set()
    for s_p in s_points.split():
        p = eval(s_p)
        if p < n_points: points.add(p)
    return points

def change_arc_lines(file_lines, R_new):        
    file_lines = [scale_point_inline(line, R_new) if line.find('arc')>=0 else line for line in file_lines]
            
    return file_lines
        
def scale_point_inline(line, R_new):
    ar_s = re.search('(?<=\()[\d.,\ \-]+(?=\))', line)[0]
    
    delimiter = ',' if ar_s.find(',') >= 0 else ' '
    ar = [eval(s) for s in ar_s.split(delimiter)]
    #to do: now we can scale by multiplying by R_new since center of cylinder = 0, 0. It will be different if it's not true
    ar[0], ar[1] = R_new*ar[0], R_new*ar[1]
    
    ar_s_new = str(ar)[1:-1] if ar_s.find(',') >= 0 else str(ar).replace(',', '')[1:-1]
    line= re.sub('(?<=\()[\d.,\ \-]+(?=\))', ar_s_new, line)
    return line

def scale_upper_points(file_lines, start):
    #changes x-coord of the points 18 and 7 accoding to their cylindric counterparts
    point_map = {18:15, 7:4}
    for upper_p, cyl_p in point_map.items():
        x_new = re.search('(?<=\()[\d.\-]+', file_lines[cyl_p+start])[0]
        file_lines[upper_p+start] = re.sub('(?<=\()[\d.\-]+', x_new, file_lines[upper_p+start])

def scale_side_points(file_lines, start):
    #changes y-coord of the points 14 and 3 accoding to their cylindric counterparts
    cyl_p = 4
    y_new = re.search('(?<=\ )[\d.\-]+(?=\,)', file_lines[cyl_p+start])[0]
    for i in [3, 14]:
        file_lines[i+start] = re.sub('(?<=\ )[\d.\-]+(?=\,)', y_new, file_lines[i+start])
        

