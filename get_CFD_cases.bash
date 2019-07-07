root_path=$PWD

R0="0.25"
dR="0.05"
nR="2"
V0="1"
dV="0.5"
nV="2"

dirname="cylinder_${nR}x${nV}_R=(${R0}..${dR})_V=(${V0}..${dV})"
mkdir $dirname
cd $dirname

cp -r $FOAM_TUTORIALS/basic/potentialFoam/cylinder/ .
mv cylinder orig
mv orig/0.orig orig/0

python3 $root_path/Lib/preprocessor.py $R0 $dR $nR $V0 $dV $nV

for D in *; do
	if [ -d "${D}" ]; then
        if [[ "${D}" == *"R="* && "${D}" != *"_NN" ]]; then
			blockMesh -case "${D}"
			potentialFoam -case $PWD/"${D}"
			postProcess -case $PWD/"${D}" -func 'components(U)' 
			postProcess -case $PWD/"${D}" -func writeCellCentres
		fi
	fi
done

# writes data in the CSV file "data.csv" where each point represents a row = [ux, uy, cx, cy, v_in]
python3 $root_path/Lib/postprocessor.py

