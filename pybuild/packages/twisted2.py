from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Twisted2(Package):
    source = GitSource('https://github.com/QPYPI/twisted.git', alias='twisted2', branch='qpyc-18.7.0')
    patches = [
        #LocalPatch('0001-cross-compile'),
    ]

    def prepare(self):
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        I_FLAG = f'-I../../build/target/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}'\
            ':../../build/target/openblas/usr/include'
        L_FLAG = f'-L../../build/target/python{PY_BRANCH}/usr/lib'\
            ':../../build/target/openblas/usr/lib'\
            f':{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm'
        LIB = f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m'
        self.run([
            'python2',
            'setup.py',
            'build_ext',
            I_FLAG,
            L_FLAG,
            LIB
        ])
        self.run([
            'python2',
            'setup.py',
            'build_clib'
        ])

        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_scripts',
        ])
