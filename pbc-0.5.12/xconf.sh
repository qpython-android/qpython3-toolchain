TARGET=arm-linux-androideabi
pushd ../thirdparty
TARGET_DIR=`pwd`
popd
push ../gmp-5.0.2
GMP_DIR=`pwd`
popd

# Relative paths gave me heartburn...
export CPPFLAGS='${TARGET_DIR}/include'
export LDFLAGS='${TARGET_DIR}/lib'
./configure --host=$TARGET --target=$TARGET --prefix=$PWD/compiled/$TARGET CFLAGS="-I${GMP_DIR}" 
