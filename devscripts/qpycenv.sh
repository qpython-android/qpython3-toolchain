#!/bin/bash

export ANDROID_NDK=/Users/yanhecun/Develop/crystax-ndk-10.3.2
export ANDROID_VER=21
export TARGET_ARCH_QPY=armeabi-v7a

# Set path to ndk-bundle
HST=`uname`
HST=`echo $HST|tr '[:upper:]' '[:lower:]'`

# Set the PATH to contain paths to clang and arm-linux-androideabi-* utilities
export PATH=${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin:${ANDROID_NDK}/toolchains/llvm-3.7/prebuilt/${HST}-x86_64/bin:$PATH



# Set the clang cross compile flags
export CLANG_FLAGS_QPY=" -target arm-linux-androideabi -marm -mfpu=vfp -mfloat-abi=softfp --sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm -gcc-toolchain ${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/ -I${ANDROID_NDK}/toolchains/llvm-3.7/prebuilt/${HST}-x86_64/lib/clang/3.7/include -I${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm/usr/include"

# for numpy

# Set LDFLAGS so that the linker finds the appropriate libgcc
export LDFLAGS="-L${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/lib/gcc/arm-linux-androideabi/4.9 -L${ANDROID_NDK}/sources/crystax/libs/${TARGET_ARCH_QPY}"
export CC="${ANDROID_NDK}/toolchains/llvm-3.7/prebuilt/darwin-x86_64/bin/clang  ${CLANG_FLAGS_QPY} ${LDFLAGS}"
export CXX="${ANDROID_NDK}/toolchains/llvm-3.7/prebuilt/darwin-x86_64/bin/clang++  ${CLANG_FLAGS_QPY} ${LDFLAGS}"
export RANLIB="arm-linux-androideabi-ranlib"
export AR="arm-linux-androideabi-ar"
#export LD="arm-linux-androideabi-ld ${LDFLAGS}"
#export LDSHARED="arm-linux-androideabi-ld ${LDFLAGS} -shared"
