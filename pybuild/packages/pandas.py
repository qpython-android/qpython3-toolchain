from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Pandas(Package):
    source = GitSource('https://github.com/AIPYX/pandas.git', alias='pandas', branch='qpyc/0.23.4')
    patches = [
        #LocalPatch('0001-cross-compile'),
        #LocalPatch('0001-add-ftello64'),
    ]

    #use_gcc = True

    def prepare(self):
        #self.run(['cp', self.filesdir / 'site.cfg', './'])
        pass

    def build(self):
        #self.system("find . -iname '*.pyx' -exec cython {} \;")
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        self.run([
            'python',
            'setup.py',
            'cython',
        ])

        self.run([
            'python',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}'\
            f':../../build/target/openblas/usr/include'\
            f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include'\
            f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include',
            f'-L../../build/target/python/usr/lib'\
            f':../../build/target/openblas/usr/lib:{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm'\
            f':{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a'\
            f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a'\
            f':{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m,gnustl_static,atomic'
        ])

        self.run([
            'python',
            'setup.py',
            'build_py',
        ])

    def refresh(self):
        return True
