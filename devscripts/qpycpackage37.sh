#!/bin/bash
#
# This script could export the QPython3's asset file like private(x).mp3
# @Author: River
#

# Please set the correct STRIP for your platform
HST=`uname`
HST=`echo $HST|tr '[:upper:]' '[:lower:]'`

STRIP=${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin/arm-linux-androideabi-strip

ROOT=`pwd`
DST=${ROOT}/build/qpyc37
PYSRC=${ROOT}/build/target/python
ASSRC=${ROOT}/mk/qpyc3
mkdir -p $DST


OPENBLAS_SO=${ROOT}/build/target/openblas/usr/lib/libopenblas.so
NUMPY_LIB=${ROOT}/src/numpy/build/lib.linux-x86_64-3.7/numpy
NUMPY_SRC=${ROOT}/src/numpy/build/src.linux-x86_64-3.7/numpy
SCIPY_LIB=${ROOT}/src/scipy/build/lib.linux-x86_64-3.7/scipy
SCIPY_SRC=${ROOT}/src/scipy/build/src.linux-x86_64-3.7/scipy



# clean old resources
cd $DST && rm -fr *

echo Python3.7.0 > PY3VER


# Init dir structures

DIRS="
bin
include
include/python3.7m
lib
lib/python3.7
lib/python3.7/config-3.7m
lib/python3.7/lib-dynload
lib/python3.7/site-packages
"

for item in $DIRS
    do echo $item;
    mkdir -p $item
done

find ${PYSRC} -name __pycache__ -exec rm -fr {} \;

# Copy resources
#cp ${ANDROID_NDK}/sources/crystax/libs/armeabi-v7a/libcrystax.so $DST/lib
cp ${PYSRC}/usr/bin/python3.7m $DST/bin/python3-android5
#cp ${PYSRC}/usr/lib/libpython3.so $DST/lib
#cp ${PYSRC}/usr/lib/libpython3.7m.so.1.0 $DST/lib

cp $ASSRC/bin/* $DST/bin
touch $DST/lib/python3.7/config-3.7m/Makefile
touch $DST/include/python3.7m/pyconfig.h
cp ${PYSRC}/usr/lib/python3.7/lib-dynload/* $DST/lib/python3.7/lib-dynload
cd ${PYSRC}/usr/lib/python3.7 &&  zip -r $DST/lib/python37.zip * --exclude lib-dynload

# Copy python packages (numpy)
cp ${OPENBLAS_SO} $DST/lib
$STRIP $DST/lib/*.so

cp -r $NUMPY_LIB $DST/lib/python3.7/site-packages/numpy
cp -r $SCIPY_LIB $DST/lib/python3.7/site-packages/scipy

cp $NUMPY_SRC/__config__.py $DST/lib/python3.7/site-packages/numpy/__config__.py
cp $SCIPY_SRC/__config__.py $DST/lib/python3.7/site-packages/scipy/__config__.py


# Strip
$STRIP $DST/bin/python3-android5
find $DST -name "*.so" -exec $STRIP {} \;

# Package
cd $DST && tar -czvf ../qpyc37.mp3 *
