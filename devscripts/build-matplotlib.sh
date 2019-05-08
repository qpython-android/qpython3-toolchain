#cd /root/qpython3-toolchain/src/matplotlib2/build/lib.linux-x86_64-2.7 find . -name "*.so" -exec arm-linux-androideabi-strip {} \; && tar -czvf matplotlib.tgz matplotlib  mpl_toolkits  pylab.py
cd /root/qpython3-toolchain/src/matplotlib/build/lib.linux-x86_64-3.6 find . -name "*.so" -exec arm-linux-androideabi-strip {} \; && tar -czvf matplotlib.tgz matplotlib  mpl_toolkits  pylab.py
