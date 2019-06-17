cd src/pycryptodome/build/lib.linux-x86_64-3.6 && find . -name "*.so" -exec arm-linux-androideabi-strip {} \;
tar -czvf pycryptodome.tgz Crypto
