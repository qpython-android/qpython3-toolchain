TARGET=arm-linux-androideabi
pushd ../thirdparty
export TARGET_DIR=`pwd`
popd

export CC=${TARGET}-gcc
export CXX=${TARGET}-g++
export AR=${TARGET}-ar
export RANLIB=${TARGET}-ranlib 
export LD=${TARGET}-ld
export NM=${TARGET}-nm

mv Makefile tmp && cp tmp Makefile && rm tmp

make && make install

