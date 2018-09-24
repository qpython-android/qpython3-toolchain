from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class H5py2(Package):
    source = GitSource('https://github.com/AIPYX/h5py.git', alias='h5py2', branch='qpyc/2.8.0')
    patches = [
        #LocalPatch('0001-cross-compile'),
    ]

    def prepare(self):
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        NDK = self.env["ANDROID_NDK"]
        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}'\
            ':../../build/target/openblas/usr/include'\
            ':../../src/hdf5/src'\
            ':../../src/hdf5/hl/src',
            f'-L../../build/target/python{PY_BRANCH}/usr/lib'\
            ':../../build/target/openblas/usr/lib'\
            f':{NDK}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
