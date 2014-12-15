set -e

TARGET=${TARGET:-"arm-linux-androideabi"}
pushd ../thirdparty
export TARGET_DIR=`pwd`
popd

export CC=${TARGET}-gcc
export CXX=${TARGET}-g++
export AR=${TARGET}-ar
export RANLIB=${TARGET}-ranlib 
export LD=${TARGET}-ld
export NM=${TARGET}-nm

export SYSTEM="Linux"
export MACHINE="i686"

./config --prefix=${TARGET_DIR}

mv Makefile tmp && cp tmp Makefile && rm tmp

make && make install

