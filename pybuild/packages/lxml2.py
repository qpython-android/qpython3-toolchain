from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Lxml2(Package):
    source = GitSource('https://github.com/QPYPI/lxml.git', alias='lxml2', branch='qpyc-4.2.5')
    patches = [
        #LocalPatch('0001-cross-compile'),
    ]

    def prepare(self):
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        BLD = os.path.join(os.getcwd(),'build/target')
        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I{BLD}/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}'\
            f':{BLD}/libxslt/include'\
            f':{BLD}/libxml2/include/libxml2',
            f'-L{BLD}/python{PY_BRANCH}/usr/lib'\
            f':{BLD}/libxml2/lib'\
            f':{BLD}/libxslt/lib'\
            f':{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
