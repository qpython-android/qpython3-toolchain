echo "Cleaning all Py34a"
echo "openssl"
pushd openssl
make clean
popd
echo "Sqlite3"
pushd sqlite3
make clean
popd
echo "zlip"
pushd zlib-1.2.6
make clean
popd
echo "bz2"
pushd bzip2-1.0.6
make clean
popd
echo "ncurses"
pushd ncurses-5.9
make clean
popd
echo "readline"
pushd readline-6.2
make clean
popd
echo "gmp"
pushd gmp-5.0.2
make clean
popd
echo "pbc"
pushd pbc-0.5.12
make clean
popd
echo "Python 3"
pushd python3-src
make clean
rm -rf _install build android
popd
echo "Third party"
pushd thirdparty
rm -rf *
echo "Cross-compiled third party libraries go here." >README
echo "And done."
