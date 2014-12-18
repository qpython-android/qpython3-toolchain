#!/bin/bash
echo "Building all Py34a"

set -e

export TARGET="i686-linux-android"

arch=`uname -m`
if [ "$arch" == "i686" ]
then
    # This is really an ubuntu fix, but shouldn't mess anything else up.
    export LDFLAGS="-L/usr/lib/i386-linux-gnu/"
fi

echo "openssl"
pushd openssl
./xbuild.sh
popd
echo "Sqlite3"
pushd sqlite3
./xbuild.sh
popd
echo "zlib"
pushd zlib-1.2.6
./xbuild.sh
popd
echo "bz2"
pushd bzip2-1.0.6
./xbuild.sh
popd
echo "ncurses"
pushd ncurses-5.9
./xbuild.sh
popd
echo "readline"
pushd readline-6.2
./xbuild.sh
popd
#echo "gmp"
#pushd gmp-5.0.2
#./xbuild.sh
#popd
#echo "pbc"
#pushd pbc-0.5.12
#./xbuild.sh
#popd
echo "Python 3"
pushd python3-src
./xbuild.sh
popd

echo "And done."
