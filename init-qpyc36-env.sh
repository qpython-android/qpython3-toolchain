#export ANDROID_NDK=~/Develop/android-ndk-r16b
export ANDROID_NDK=/Users/yanhecun/Develop/crystax-ndk-10.3.2
export ANDROID_VER=21
export CRYSTAX_TARGET_ARCH='armeabi-v7a'
## init for openblas


# Set path to ndk-bundle
HST=`uname`
HST=`echo $HST|tr '[:upper:]' '[:lower:]'`

# Set the PATH to contain paths to clang and arm-linux-androideabi-* utilities
export PATH=${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin:${ANDROID_NDK}/toolchains/llvm-3.7/prebuilt/${HST}-x86_64/bin:$PATH

# Set LDFLAGS so that the linker finds the appropriate libgcc
export LDFLAGS="-L${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/lib/gcc/arm-linux-androideabi/4.9 -L${ANDROID_NDK}/sources/crystax/libs/${CRYSTAX_TARGET_ARCH}"

# Set the clang cross compile flags
export CLANG_FLAGS_OPENBLAS="-v -target arm-linux-androideabi -marm -mfpu=vfp -mfloat-abi=softfp --sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm -gcc-toolchain ${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/"
export AR_OPENBLAS=${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin/arm-linux-androideabi-gcc-ar


# for numpy
export CC="arm-linux-androideabi-gcc -DANDROID -mandroid -fomit-frame-pointer --sysroot ${ANDROID_NDK}/platforms/android-${ANDROID_VER}/arch-arm -L${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/lib/gcc/arm-linux-androideabi/4.9 -I${ANDROID_NDK}/toolchains/x86_64-4.9/prebuilt/${HST}-x86_64/lib/gcc/x86_64-linux-android/4.9/include"
export AR=${AR_OPENBLAS}
export RANLIB="arm-linux-androideabi-ranlib"
export LD="${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin/arm-linux-androideabi-ld -L/Users/yanhecun/QPYTHON/qpython3-core/build/target/python/usr/lib /Users/yanhecun/Develop/crystax-ndk-10.3.2/toolchains/x86_64-4.9/prebuilt/darwin-x86_64/lib/gcc/x86_64-linux-android/4.9 -lpython36m"
export LDSHARED="${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin/arm-linux-androideabi-ld -L/Users/yanhecun/QPYTHON/qpython3-core/build/target/python/usr/lib /Users/yanhecun/Develop/crystax-ndk-10.3.2/toolchains/x86_64-4.9/prebuilt/darwin-x86_64/lib/gcc/x86_64-linux-android/4.9 -lpython36m -shared"
#export LDSHARED="${ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/${HST}-x86_64/bin/arm-linux-androideabi-ld -shared -L/Users/yanhecun/QPYTHON/qpython3-core/build/target/python/usr/lib -lpython36m"
