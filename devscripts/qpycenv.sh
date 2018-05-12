#!/bin/bash

export ANDROID_NDK=/home/QPY/android-ndk-r13b
export ANDROID_VER=21
export TARGET_ARCH_QPY=armeabi-v7a

# Set path to ndk-bundle
HST=`uname`
HST=`echo $HST|tr '[:upper:]' '[:lower:]'`

# Set the PATH to contain paths to clang and arm-linux-androideabi-* utilities
export PATH=${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin:${ANDROID_NDK}/toolchains/llvm/prebuilt/${HST}-x86_64/bin:$PATH



export CC_FLAGS_QPY=" -marm -mfpu=vfp -mfloat-abi=softfp -std=gnu11 --sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm -I${ANDROID_NDK}/sysroot/usr/include -I${ANDROID_NDK}/sysroot/usr/include/arm-linux-androideabi -D__ANDROID_API__=21"
export CLANG_FLAGS_QPY=" -femulated-tls -target arm-linux-androideabi -marm -mfpu=vfp -mfloat-abi=softfp --sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm -gcc-toolchain ${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/ -I${ANDROID_NDK}/sysroot/usr/include -I${ANDROID_NDK}/sysroot/usr/include/arm-linux-androideabi -D__ANDROID_API__=21"

export LDFLAGS="--sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm -L${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm/usr/lib -L${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/lib/gcc/arm-linux-androideabi/4.9 -L${ANDROID_NDK}/toolchains/renderscript/prebuilt/${HST}-x86_64/platform/arm -lm -lgcc -lc -ldl"

export CC="arm-linux-androideabi-gcc ${CC_FLAGS_QPY} ${LDFLAGS}"
export CXX="arm-linux-androideabi-g++ ${CC_FLAGS_QPY} ${LDFLAGS}"
#export CC="${ANDROID_NDK}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang ${CLANG_FLAGS_QPY} ${LDFLAGS}"
#export CXX="${ANDROID_NDK}/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++ ${CLANG_FLAGS_QPY} ${LDFLAGS}"

export RANLIB="arm-linux-androideabi-ranlib"
export AR="arm-linux-androideabi-ar"
export AS="arm-linux-androideabi-as"
export LD="arm-linux-androideabi-ld"
#export LDSHARED="arm-linux-androideabi-ld ${LDFLAGS} -shared"

export FC="arm-linux-androideabi-gfortran -DANDROID -mandroid --sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm"
