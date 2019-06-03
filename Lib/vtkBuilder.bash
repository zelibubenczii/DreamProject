for D in *; do
    # echo "${D}"
	if [ -d "${D}" ]; then
        if [[ "${D}" == *"_NN" ]]; then
            # preD=${D/_NN/}
            # echo $preD
            # cp -r $preD/. $D
            python3 Lib/caseArgSetter.py $D
        fi
    fi
done