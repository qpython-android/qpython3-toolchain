from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Pycryptodome(Package):
    source = GitSource('https://github.com/QPYPI/pycryptodome.git', alias='pycryptodome', branch='qpyc/v3.8.1')
    patches = [
        #LocalPatch('0001-cross-compile'),
        #LocalPatch('0001-add-ftello64'),
    ]

    #use_gcc = True

    def prepare(self):
        #self.run(['cp', self.filesdir / 'site.cfg', './'])
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        self.run([
            'python',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}:../../build/target/openblas/usr/include',
            f'-L../../build/target/python/usr/lib:../../build/target/openblas/usr/lib',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python',
            'setup.py',
            'build_py',
        ])
