from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Theano2(Package):
    source = GitSource('https://github.com/AIPYX/theano.git', alias='theano2', branch='qpyc/1.0.3')
    patches = [
        #LocalPatch('0001-cross-compile'),
        #LocalPatch('0001-add-ftello64'),
    ]

    def prepare(self):
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}'\
            ':../../build/target/openblas/usr/include',
            f'-L../../build/target/python{PY_BRANCH}/usr/lib'\
            ':../../build/target/openblas/usr/lib:'\
            '{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
