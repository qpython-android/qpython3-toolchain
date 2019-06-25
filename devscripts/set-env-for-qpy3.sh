#!/bin/bash

pyenv global 3.6.6

export ANDROID_SDK=/home/QPY/android-sdk-20140702
export ANDROID_NDK=/home/QPY/android-ndk-r17
export ANDROID_NDK_GFORTRAN=/home/QPY/android-ndk-r13b
export ANDROID_VER=21
#export TARGET_ARCH_QPY=armeabi-v7a
export TARGET_ARCH_QPY=arm64-v8a
export TARGET_ARCH_ANDROID=aarch64 # aarch64 / arm
export TARGET_ARCH_INCLUDE=arm64 # arm64 / arm
export TARGET_ARCH_NAME=android # android / androideabi 
export PY_BRANCH="3" # or 3
export PY_M_BRANCH="6m" # or 6m

# Set path to ndk-bundle
HST=`uname`
HST=`echo $HST|tr '[:upper:]' '[:lower:]'`

# Set the PATH to contain paths to clang and arm-linux-androideabi-* utilities
export PATH=${ANDROID_NDK}/toolchains/${TARGET_ARCH_ANDROID}-linux-${TARGET_ARCH_NAME}-4.9/prebuilt/${HST}-x86_64/bin:${ANDROID_NDK}/toolchains/llvm/prebuilt/${HST}-x86_64/bin:$PATH


export CLANG_FLAGS_BASE="  -fno-integrated-as -femulated-tls -target ${TARGET_ARCH_ANDROID}-linux-${TARGET_ARCH_NAME} -m${TARGET_ARCH_INCLUDE} -mfpu=vfp -mfloat-abi=softfp --sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-${TARGET_ARCH_INCLUDE} -gcc-toolchain ${ANDROID_NDK}/toolchains/${TARGET_ARCH_ANDROID}-linux-${TARGET_ARCH_NAME}-4.9/prebuilt/${HST}-x86_64/ -I${ANDROID_NDK}/sysroot/usr/include -I${ANDROID_NDK}/sysroot/usr/include/${TARGET_ARCH_ANDROID}-linux-${TARGET_ARCH_NAME} -D__ANDROID_API__=21"
export CLANG_FLAGS_QPY="${CLANG_FLAGS_BASE} -L${ANDROID_NDK}/toolchains/renderscript/prebuilt/linux-x86_64/platform/${TARGET_ARCH_INCLUDE} -lcompiler_rt"

export CC="${ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/bin/clang ${CLANG_FLAGS_QPY} -Wl,-u,__mulodi4 -Wno-error=unused-command-line-argument ${LDFLAGS}"
export CXX="${ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++  ${CLANG_FLAGS_QPY} -fno-integrated-as -femulated-tls -target ${TARGET_ARCH_ANDROID}-linux-${TARGET_ARCH_NAME} -m${TARGET_ARCH_INCLUDE} -mfpu=vfp -mfloat-abi=softfp -I${ANDROID_NDK}/sources/cxx-stl/gnu-libstdc++/4.9/include -I. -I${ANDROID_NDK}/sources/cxx-stl/gnu-libstdc++/4.9/libs/${TARGET_ARCH_QPY}/include ${CLANG_FLAGS_BASE} -Wall -Wno-error=c++11-extensions -Wno-error=gnu-anonymous-struct -Wno-error=nested-anon-types -Wno-error=deprecated-declarations -Wno-error=unused-function -Wno-error=variadic-macros -Wno-error=zero-length-array -Wno-error=c++11-long-long -Wno-error=gcc-compat -Wno-error=unused-command-line-argument ${LDFLAGS} -L${ANDROID_NDK}/sources/cxx-stl/gnu-libstdc++/4.9/libs/${TARGET_ARCH_QPY} -latomic "

export FC="${TARGET_ARCH_ANDROID}-linux-${TARGET_ARCH_NAME}-gfortran -DANDROID -mandroid --sysroot ${ANDROID_NDK_GFORTRAN}/platforms/android-${ANDROID_VER}/arch-${TARGET_ARCH_INCLUDE}"
