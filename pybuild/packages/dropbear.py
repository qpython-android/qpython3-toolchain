from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class Dropbear(Package):
    source = GitSource('https://github.com/QPYPI/dropbear.git', alias='dropbear', branch='qpyc-2018.76')
    patches = [
        #LocalPatch('0001-Fix-libtoolize-s-issue-in-autogen.sh'),
    ]

    skip_uploading = True
    re_configure = True

    def prepare(self):
        pass

    def build(self):
        import os
        ANDROID_NDK = os.getenv('ANDROID_NDK')
        CLANG_FLAGS_QPY = os.getenv('CLANG_FLAGS_QPY')
        CC = f"{ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/bin/clang {CLANG_FLAGS_QPY}"
        BLD = os.path.join(os.getcwd(),'build/target')

        self.system(f'autoconf; autoheader')
        self.system(f'CC=\"{CC}\" CXX=\"{os.getenv("CXX")}\" LDFLAGS=\"-lgnustl_static -L{ANDROID_NDK}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a -L{ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a\" '\
        f'./configure --host=arm-linux-androideabi --target=arm-linux-androideabi --disable-largefil --disable-syslog --disable-shadow --disable-lastlog --disable-utmp --disable-utmpx --disable-wtmp --disable-wtmpx --disable-loginfunc --disable-pututline --disable-pututxline --with-zlib={BLD}/zlib --prefix={self.destdir()}')
        self.system(f'make install')

        
    def fresh(self):
        return True
