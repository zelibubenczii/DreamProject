root_path=$PWD

R0="1"
dR="0.1"
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
