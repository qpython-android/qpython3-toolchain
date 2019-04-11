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
        BLD = os.path.join(os.getcwd(),'build/target')
        ANDROID_NDK = os.getenv("ANDROID_NDK")

        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I{BLD}/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}'\
            ':{BLD}/openblas/usr/include',
            f'-L{BLD}/python{PY_BRANCH}/usr/lib'\
            ':{BLD}/openblas/usr/lib'\
            ':{ANDROID_NDK}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
        self.run([
            'python2',
            'setup.py',
            'install',
            '--root',
            f'{BLD}/python{PY_BRANCH}',
        ])
