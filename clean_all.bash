protected_folders=(Lib Help)

for entry in *
do
    if [[ ! " ${protected_folders[@]} " =~ " ${entry} " ]]; then
        if [[ "$entry" != *".bash" && "$entry" != *"_NN" ]]; then
            rm -r "${entry}"
        fi
    fi
done
