from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Matplotlib(Package):
    source = GitSource('https://github.com/AIPYX/matplotlib.git', alias='matplotlib', branch='qpyc/v2.2.3')
    patches = [
        #LocalPatch('0001-cross-compile'),
        #LocalPatch('0001-add-ftello64'),
    ]

    #use_gcc = True

    def prepare(self):
        self.run(['cp', self.filesdir / 'setup.cfg', './'])

    def build(self):
        #self.system("find . -iname '*.pyx' -exec cython {} \;")
        JNIR = os.path.join(self.filesdir, '../../mk/pygamesdl2/jni')
        JNIL = os.path.join(self.filesdir, '../../mk/pygamesdl2/libs/armeabi-v7a')
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        self.run([
            'python',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}:../../build/target/openblas/usr/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include:{JNIR}/png:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include',
            f'-L../../build/target/python/usr/lib:../../build/target/openblas/usr/lib:{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm:{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a:{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a:{JNIL}',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m,gnustl_static,atomic',
            f'-p androideabi'
        ])
        #:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include
        #{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a:

        self.run([
            'python',
            'setup.py',
            'build_py',
        ])

    def refresh(self):
        return True
