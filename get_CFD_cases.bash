root_path=$PWD

R0="0.5"
dR="0.05"
nR="3"
V0="2"
dV="0.5"
nV="3"

python $root_path/Lib/preprocessor.py $R0 $dR $nR $V0 $dV $nV

dirname="cylinder_V0=${V0}_dV=${dV}_N=${N}"
mkdir $dirname
cd $dirname

cp -r $FOAM_TUTORIALS/basic/potentialFoam/cylinder/ .
mv cylinder orig
mv orig/0.orig orig/0

# python Lib/preprocessor.py u_inp_0 delta_u N
python $root_path/Lib/preprocessor.py $R0 $dR $nR $V0 $dV $nV

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

# writes data in the CSV file "data.csv" where each point represents a row = [ux, uy, cx, cy, v_in]
python3 $root_path/Lib/postprocessor.py

