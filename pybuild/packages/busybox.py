from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class Busybox(Package):
    source = GitSource('https://github.com/QPYPI/busybox.git', alias='busybox')
    patches = [
        #LocalPatch(''),
    ]

    skip_uploading = True
    re_configure = True

    def prepare(self):
        pass

    def build(self):
        import os
        #self.system(f'./autogen.sh')
        #self.system(f'CC=\"{os.getenv("CC")}\" CXX=\"{os.getenv("CXX")}\" LDFLAGS=\"-lgnustl_shared -lsupc++ -latomic -L{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a\" ./configure --host=arm-linux-androideabi --target=arm-linux-androideabi --prefix={self.destdir()}')
        self.system(f'make menuconfig')
        self.system(f'make')
        self.system(f'make install')
        #self.run_with_env(['make', 'install', f'PREFIX={self.destdir()}/usr'])
        #self.system(
        #    f'if [ -e {self.destdir()}/lib/libzmq.so ] ; then mv {self.destdir()}/lib/libzmq.so {self.destdir()}/lib/libzmq.so.old; fi'
        #)

    def fresh(self):
        return True
