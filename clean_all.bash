protected_files=(clean_all clean_all.bash run_all run_all.bash Lib README.md)

for entry in *
do
    if [[ ! " ${protected_files[@]} " =~ " ${entry} " ]]; then
        rm -r "${entry}"
    fi
done
