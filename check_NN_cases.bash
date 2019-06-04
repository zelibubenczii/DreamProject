#changes cases file in each folder ends with "_NN" according to csv file in the "_CSV" folder
Lib/VtkBuilder.bash

#get contours of velocity Ux.jpg and U_y.jpg in each folder which ends with *"_NN" (neural network case)
for D in *; do
    if [ -d "${D}" ] && [[ "${D}" == *"_NN" ]]; then
        foamToVTK -case "${D}"
        pvbatch Lib/paraView/getContoursUxUy.py
    fi
done