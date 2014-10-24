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
./configure LDFLAGS="-L${TARGET_DIR}/lib" CPPFLAGS="-I${TARGET_DIR}/include" --host=${TARGET} --target=${TARGET} --prefix=${TARGET_DIR} && make && make install
