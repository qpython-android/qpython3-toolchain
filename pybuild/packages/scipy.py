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
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        LD_FLAG=f'-shared -DANDROID --sysroot {self.env["ANDROID_NDK"]}/platforms/android-21/arch-arm -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a'
        PY_FLAG=f'-I../../build/target/python/usr/include/python3.6m'\
        f':../../build/target/openblas/usr/include'\
        f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include'\
        f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include '\
        f'-L../../build/target/python/usr/lib'\
        f':../../build/target/openblas/usr/lib:'\
        f'../numpy/build/temp.linux-x86_64-3.6:'\
        f'{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a '\
        f':{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a'\
        f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a '\
        f'-lopenblas,python3.6m,gcc,m,gnustl_static,atomic'

        self.system( 
            f'LDFLAGS=\" {LD_FLAG} \" python setup.py build_ext {PY_FLAG}' 
        )
        self.system( 
            f'LDFLAGS=\" {LD_FLAG} \" python setup.py build_clib {PY_FLAG}' 
        )
        self.run([
            'python',
            'setup.py',
            'build_py',
        ])
