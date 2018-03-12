#!/bin/bash
#
# This script could export the QPython3's asset file like private(x).mp3
# @Author: River
#

# Please set the correct STRIP for your platform
STRIP=${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64/bin/arm-linux-androideabi-strip

ROOT=`pwd`
DST=${ROOT}/build/qpyc36
PYSRC=${ROOT}/build/target/python
ASSRC=${ROOT}/mk/qpyc3
mkdir -p $DST

# clean old resources
cd $DST && rm -fr *

echo Python3.6.4 > PY3VER


# Init dir structures

DIRS="
bin
include
include/python3.6m
lib
lib/python3.6
lib/python3.6/config-3.6m
lib/python3.6/lib-dynload
lib/python3.6/site-packages
"

for item in $DIRS
    do echo $item;
    mkdir -p $item
done

find ${PYSRC} -name __pycache__ -exec rm -fr {} \;

# Copy resources
cp ${PYSRC}/usr/bin/python3.6m $DST/bin/python3-android5
cp $ASSRC/bin/* $DST/bin
touch $DST/lib/python3.6/config-3.6m/Makefile
touch $DST/include/python3.6m/pyconfig.h
cp ${PYSRC}/usr/lib/python3.6/lib-dynload/* $DST/lib/python3.6/lib-dynload
cd ${PYSRC}/usr/lib/python3.6 &&  zip -r $DST/lib/python36.zip * --exclude lib-dynload

# Strip
$STRIP $DST/bin/python3-android5
find $DST/lib/python3.6/lib-dynload -name "*.so" -exec $STRIP {} \;

# Package
cd $DST && tar -czvf ../qpyc3.mp3 *

