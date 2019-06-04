cp -r $FOAM_TUTORIALS/basic/potentialFoam/cylinder/ .
mv cylinder orig
mv orig/0.orig orig/0

# python Lib/preprocessor.py u_inp_0 delta_u N
python Lib/preprocessor.py 1 0.2 2

for D in *; do
	if [ -d "${D}" ]; then
        if [[ "${D}" == *"V_in"* && "${D}" != *"_NN" ]]; then
			blockMesh -case "${D}"
			potentialFoam -case $PWD/"${D}"
			postProcess -case $PWD/"${D}" -func 'components(U)' 
			postProcess -case $PWD/"${D}" -func writeCellCentres
		fi
	fi
done

# writes data in the CSV file "data.csv" where each point represents a row = [ux/v_in, uy/v_in, cx, cy, v_in]
python3 Lib/postprocessor.py

