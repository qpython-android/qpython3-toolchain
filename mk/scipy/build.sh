python setup.py build_ext --fcompiler arm-linux-androideabi-gfortran -I../../build/target/python/usr/include/python3.6m:../../build/target/openblas/usr/include:/home/QPY/android-ndk-r13b/sources/cxx-stl/gnu-libstdc++/4.9/include:/home/QPY/android-ndk-r13b/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi/include -L../../build/target/python/usr/lib:../../build/target/openblas/usr/lib:../numpy/build/temp.linux-x86_64-3.6 -lopenblas,python3.6m,m,gfortran