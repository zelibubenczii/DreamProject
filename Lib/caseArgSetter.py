import os, re, csv, fileinput, sys
from postprocessor import read_data

def set_U_i(folder_path, data_id):
    """
    takes the data (represented as a list of strings, i.e. a part of an opeanFoam file,
    and changes the corresponding values in each string)
    """
    
    data_files = ['U_test.csv', 'U_pr.csv', 'E.csv']
    
    with open(folder_path+'/_CSV/' + data_files[data_id], 'r') as f:
        reader = csv.reader(f)
        U_new = list(reader)
        
    for i, x_i in enumerate(['x', 'y', '']):        
        U_file_path = folder_path + '/0/U' + x_i
        _, start = read_data(U_file_path)
        for j, line in enumerate(fileinput.input(U_file_path, inplace='True')):     
            if len(x_i) > 0:
                if j >= start and j - start < len(U_new):
                    line = str(eval(U_new[j-start][i])) + '\n'

            else:
                if j >= start and j - start < len(U_new):
                    # line = U_new[j-start].replace('[', '(').replace(']', ')').replace(',', '')
                    line = "({} {} {})".format(*U_new[j-start]) + '\n'
            print(line, end='')
    
    # for idx, x_i in enumerate(['x', 'y']):
        # U_file_path = folder_path + '/0/U' + x_i
        # for idx, line in enumerate(fileinput.input(U_file_path, inplace='True')):     
            # if idx >= start and idx - start < len(U_new):
                # line = str(eval(U_new[idx-start][idx]))
            # print(line.rstrip())

# def change_parameters(folder_path):
    #set_U_i
    
def change_template(dir_path, data_id):
    # dir_path = argv[1]
    templates = ["draw_U_test.py", "draw_U_pr.py", "draw_E.py"]
    dir_name = os.path.basename(dir_path)
    temp_path = dir_path + '/_paraview/' + templates[data_id]
    for line in fileinput.input(temp_path, inplace='True'):
        line = line.replace('$DirPath$', dir_path).replace('$DirName$', dir_name)
        print(line, end='')

if __name__ == "__main__":
    folder_path = r"C:\Program Files\blueCFD-Core-2017\ofuser-of5\run\mlp\visualisation\R=0.7_V=3.0"
    # folder_path = sys.argv[1]
    data_id = 2
    # data_id = sys.argv[2]
    set_U_i(folder_path, data_id)
    # change_template(folder_path, data_id)
    # change_tarameters(sys.argv)
    # change_template(sys.argv)