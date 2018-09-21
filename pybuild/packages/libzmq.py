from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class LibZMQ(Package):
    source = GitSource('https://github.com/AIPYX/zeromq3-x.git', alias='libzmq', branch='qpyc/3.2.5')
    patches = [
        LocalPatch('0001-Fix-libtoolize-s-issue-in-autogen.sh'),
    ]

    skip_uploading = True
    re_configure = True

    def prepare(self):
        pass

    def build(self):
        import os
        self.system(f'./autogen.sh')
        self.system(f'CC=\"{os.getenv("CC")}\" CXX=\"{os.getenv("CXX")}\" LDFLAGS=\"-lgnustl_shared -lsupc++ -latomic -L{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a\" ./configure --host=arm-linux-androideabi --target=arm-linux-androideabi --prefix={self.destdir()}')
        self.system(f'make install')
        #self.run_with_env(['make', 'install', f'PREFIX={self.destdir()}/usr'])
        self.system(
            f'if [ -e {self.destdir()}/lib/libzmq.so ] ; then mv {self.destdir()}/lib/libzmq.so {self.destdir()}/lib/libzmq.so.old; fi'
        )

    def fresh(self):
        return True
