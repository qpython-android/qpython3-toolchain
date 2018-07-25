from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class SciPy(Package):
    source = GitSource('https://github.com/AIPYX/scipy.git', alias='scipy', branch='qpyc/v1.1.0')
    patches = [
        LocalPatch('0001-cross-compile'),
    ]

    use_gcc = True

    def prepare(self):
        self.run(['cp', self.filesdir / 'site.cfg', './'])

    def build(self):
        import os,sys
        self.system( 
            f'LDFLAGS=\" -shared -DANDROID --sysroot {self.env["ANDROID_NDK"]}/platforms/android-21/arch-arm -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a\" python setup.py build_ext -I../../build/target/python/usr/include/python3.6m:../../build/target/openblas/usr/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -L../../build/target/python/usr/lib:../../build/target/openblas/usr/lib:../numpy/build/temp.linux-x86_64-3.6:{self.env["ANDROID_NDK_GFORTRAN"]}/platforms/android-21/arch-arm/usr/lib:{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -lopenblas,python3.6m,m,gcc,gfortran' 
        )
        self.run([
            'python',
            'setup.py',
            'build_py',
        ])
