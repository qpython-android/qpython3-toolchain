#!/bin/bash

export ANDROID_NDK=/Users/yanhecun/Develop/android-ndk-r16b
export ANDROID_VER=21
export TARGET_ARCH_QPY=armeabi-v7a

# Set path to ndk-bundle
HST=`uname`
HST=`echo $HST|tr '[:upper:]' '[:lower:]'`

# Set the PATH to contain paths to clang and arm-linux-androideabi-* utilities
export PATH=${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin:${ANDROID_NDK}/toolchains/llvm/prebuilt/${HST}-x86_64/bin:$PATH



export CC_FLAGS_QPY=" -marm -mfpu=vfp -mfloat-abi=softfp --sysroot ${ANDROID_NDK}/sysroot -D__ANDROID_API__=21"
export CLANG_FLAGS_QPY=" -femulated-tls -target arm-linux-androideabi -marm -mfpu=vfp -mfloat-abi=softfp --sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm -gcc-toolchain ${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/ -I${ANDROID_NDK}/sysroot/usr/include -I${ANDROID_NDK}/sysroot/usr/include/arm-linux-androideabi -D__ANDROID_API__=21"

export LDFLAGS="-L${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm/usr/lib -L${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/lib/gcc/arm-linux-androideabi/4.9"

export CC="${ANDROID_NDK}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang ${CLANG_FLAGS_QPY} ${LDFLAGS}"
export CXX="${ANDROID_NDK}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++ ${CLANG_FLAGS_QPY} ${LDFLAGS}"

export RANLIB="arm-linux-androideabi-ranlib"
export AR="arm-linux-androideabi-ar"
export LD="arm-linux-androideabi-ld"
#export LDSHARED="arm-linux-androideabi-ld ${LDFLAGS} -shared"
