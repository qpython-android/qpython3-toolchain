TARGET=arm-linux-androideabi
pushd ../thirdparty
TARGET_DIR=`pwd`
popd

export CC=${TARGET}-gcc
export CXX=${TARGET}-g++
export AR=${TARGET}-ar
export RANLIB=${TARGET}-ranlib 
export LD=${TARGET}-ld
export NM=${TARGET}-nm

./configure --host=$TARGET --target=$TARGET --prefix=$TARGET_DIR --enable-shared && make && make install

