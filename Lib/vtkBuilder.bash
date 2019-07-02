for D in *; do
	if [ -d "${D}" ]; then
        if [[ "${D}" == *"_NN" ]]; then
            preD=${D/_NN/}
            cp -r $preD/. $D            
            path=$(realpath $D)

            mkdir $path/_paraview
            cp -u Lib/paraView/UxUy_template.py $path/_paraview
            
            python3 Lib/caseArgSetter.py $path

        fi
    fi
done