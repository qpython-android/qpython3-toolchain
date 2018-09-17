from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Android2(Package):
    source = GitSource('https://github.com/QPYPI/android-kivy.git', alias='android2')
    patches = [
        #LocalPatch(''),
    ]

    def prepare(self):
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        JNIR = os.path.join(self.filesdir, '../pygamesdl2/jni')
        JNIL = os.path.join(self.filesdir, '../pygamesdl2/libs/armeabi-v7')
        JNIO = os.path.join(self.filesdir, '../pygamesdl2/obj/local/armeabi-v7a')
        self.system("find . -iname '*.pyx' -exec cython {} \;")
        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}:../../build/target/openblas/usr/include:{JNIR}',
            f'-L../../build/target/python{PY_BRANCH}/usr/lib:{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm:{self.filesdir}/libs/armeabi-v7a:{JNIL}:{JNIO}',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])

    def fresh(self):
        return True
