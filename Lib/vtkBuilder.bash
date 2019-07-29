for D in *; do
	if [ -d "${D}" ]; then
        if [[ "${D}" == *"_NN" ]]; then
            # preD=${D/_NN/}
            # cp -r $preD/. $D            
            path=$(realpath $D)

            mkdir $path/_paraview
            mkdir $path/_CSV
            mkdir $path/images
            cp -r Lib/paraView/. $path/_paraview
            
            python3 Lib/caseArgSetter.py $path 
            foamToVTK -case $path
            pvbatch $path/_paraview/draw_U_pr.py 

        fi
    fi
done