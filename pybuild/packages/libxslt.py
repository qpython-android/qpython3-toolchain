from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class Libxslt(Package):
    source = GitSource('https://github.com/QPYPI/libxslt.git', alias='libxslt', branch='qpyc-1.1.32')
    patches = [
        #LocalPatch('0001-Fix-libtoolize-s-issue-in-autogen.sh'),
    ]

    def prepare(self):
        pass

    def build(self):
        import os
        ANDROID_NDK = os.getenv('ANDROID_NDK')
        CLANG_FLAGS_QPY = os.getenv('CLANG_FLAGS_QPY')
        LIBXML2 = os.path.join(os.getcwd(),'src/libxml2')
        CC = f"{ANDROID_NDK}/toolchains/llvm/prebuilt/linux-x86_64/bin/clang {CLANG_FLAGS_QPY}"
        self.system(f'./autogen.sh')
        self.system(f'CC=\"{CC}\" CXX=\"{os.getenv("CXX")}\" LDFLAGS=\"-lgnustl_shared -L{ANDROID_NDK}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a -L{ANDROID_NDK}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a\" '\
        f'./configure --host=arm-linux-androideabi --target=arm-linux-androideabi --without-plugins --without-debug --without-crypto --without-python --with-libxml-src={LIBXML2} --prefix={self.destdir()}')
        self.system(f'make')
        self.system(f'make install')
        self.system(
            f'if [ -e {self.destdir()}/lib/libxslt.so ] ; then mv {self.destdir()}/lib/libxslt.so {self.destdir()}/lib/libxslt.so.old; fi'
        )

    def fresh(self):
        return True
