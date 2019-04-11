cd src/scipy2/build/lib.linux-x86_64-2.7
find . -name "*.so" arm-linux-androideabi-strip {} \;
tar -czvf scipy.tgz scipy
