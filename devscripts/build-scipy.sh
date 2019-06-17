cd src/scipy/build/lib.linux-x86_64-3.6
find . -name "*.so" arm-linux-androideabi-strip {} \;
tar -czvf scipy.tgz scipy
