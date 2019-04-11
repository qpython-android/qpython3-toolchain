from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Dulwich2(Package):
    source = GitSource('https://github.com/QPYPI/dulwich.git', alias='dulwich2', branch='dulwich-0.19.6')
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
            f':{BLD}/openblas/usr/include',
            f'-L{BLD}/python{PY_BRANCH}/usr/lib'\
            f':{BLD}/openblas/usr/lib'\
            f':{ANDROID_NDK}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm',
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
