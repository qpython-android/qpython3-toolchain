cd src/pyzmq/build/lib.linux-x86_64-3.6 && find . -name "*.so" -exec arm-linux-androideabi-strip {} \; && tar -czvf zmq.tar.gz zmq
