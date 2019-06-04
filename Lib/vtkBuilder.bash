for D in *; do
    # echo "${D}"
	if [ -d "${D}" ]; then
        if [[ "${D}" == *"_NN" ]]; then
            preD=${D/_NN/}
            cp -r $preD/. $D
            path=$(realpath $D)
            python3 Lib/caseArgSetter.py $path
        fi
    fi
done