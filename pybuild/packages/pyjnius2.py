from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Pyjnius2(Package):
    source = GitSource('https://github.com/QPYPI/pyjnius-qpython.git', alias='pyjnius2', branch='qpyc-1.1.1')
    patches = [
        #LocalPatch('0001-crotss-compile'),
    ]

    def prepare(self):
        #self.run(['cp', self.filesdir / 'Setup', './'])
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
            f'-L../../build/target/python{PY_BRANCH}/usr/lib:{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm:{JNIL}:{JNIO}',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])

    def fresh(self):
        return True
