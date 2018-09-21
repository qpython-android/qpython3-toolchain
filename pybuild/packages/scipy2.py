from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class SciPy2(Package):
    source = GitSource('https://github.com/AIPYX/scipy.git', alias='scipy2', branch='qpyc/v1.1.0')
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
        PY_FLAG=f'-I../../build/target/python2/usr/include/python2.7'\
        ':../../build/target/openblas/usr/include'\
        f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include'\
        f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include '\
        '-L../../build/target/python2/usr/lib'\
        ':../../build/target/openblas/usr/lib'\
        ':../numpy2/build/temp.linux-x86_64-3.6'\
        f':{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a'\
        f':{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a'\
        f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a '\
        '-lopenblas,python2.7,gcc,m,gnustl_static,atomic'

        self.system( 
            f'LDFLAGS=\" -shared -DANDROID --sysroot {self.env["ANDROID_NDK"]}/platforms/android-21/arch-arm -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L../../build/target/python2/usr/lib -L../../build/target/openblas/usr/lib -L../numpy2/build/temp.linux-x86_64-2.7 \" python2 setup.py build_ext {PY_FLAG}' 
        )
        self.system( 
            f'LDFLAGS=\" -shared -DANDROID --sysroot {self.env["ANDROID_NDK"]}/platforms/android-21/arch-arm -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L../../build/target/python2/usr/lib -L../../build/target/openblas/usr/lib\ -L../numpy2/build/temp.linux-x86_64-2.7" python2 setup.py build_clib {PY_FLAG}' 
        )

        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
