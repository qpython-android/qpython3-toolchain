set -e

TARGET=${TARGET:-"arm-linux-androideabi"}
pushd ../thirdparty
export THIRD_PARTY_DIR=`pwd`
popd
cat pyconfig.h \
| sed -e '/#define ANDROID/ d' \
| sed -e '/#define HAVE_BROKEN_MBSTOWCS/ d' \
| sed -e '7 a#define ANDROID 1' \
| sed -e '8 a#define HAVE_BROKEN_MBSTOWCS 1' \
| sed -e '/HAVE_DEV_PTMX/ c\/* #undef HAVE_DEV_PTMX *\/' \
| sed -e '/HAVE_GETHOSTBYNAME_R/ c\/* #undef HAVE_GETHOSTBYNAME_R *\/' \
| sed -e '/HAVE_MBRTOWC/ c\/* #undef HAVE_MBRTOWC *\/' \
| sed -e '/HAVE_WCSCOLL/ c\/* #undef HAVE_WCSCOLL *\/' \
| sed -e '/HAVE_WCSFTIME/ c\/* #undef HAVE_WCSFTIME *\/' \
| sed -e '/HAVE_WCSXFRM/ c\/* #undef HAVE_WCSXFRM *\/' \
| sed -e '/HAVE_SETLOCALE/ c\/* #undef HAVE_SETLOCALE *\/' \
> temp
mv temp pyconfig.h


make HOSTPYTHON=./hostpython HOSTPGEN=./Parser/hostpgen BLDSHARED="${TARGET}-gcc -shared" CROSS_COMPILE=${TARGET}- CROSS_COMPILE_TARGET=yes HOSTARCH=${TARGET} BUILDARCH=x86_64-linux-gnu && \
make install HOSTPYTHON=./hostpython BLDSHARED="${TARGET}-gcc -shared" CROSS_COMPILE=${TARGET}- CROSS_COMPILE_TARGET=yes prefix=${PWD}/_install/python3 &&\
./xpack.sh
