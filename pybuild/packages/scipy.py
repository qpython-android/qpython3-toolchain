from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class SciPy(Package):
    source = GitSource('https://github.com/AIPYX/scipy.git', alias='scipy', branch='qpyc/v1.1.0')
    patches = [
        #LocalPatch('0001-cross-compile'),
    ]

    use_gcc = True

    def prepare(self):
        pass

    def build(self):
        import os,sys
        self.run_with_env([
            'python',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python/usr/include/python3.6m:../../build/target/openblas/usr/include',
            f'-L../../build/target/python/usr/lib:../../build/target/openblas/usr/lib',
            f'-lopenblas',
        ])
        self.run([
            'python',
            'setup.py',
            'build_py',
        ])
