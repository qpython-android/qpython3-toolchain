from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class NumPy(Package):
    source = GitSource('https://github.com/AIPYX/numpy.git', alias='numpy', branch='qpyc/v1.14.3')
    patches = [
        LocalPatch('0001-cross-compile'),
    ]

    use_gcc = True

    def prepare(self):
        self.run(['cp', self.filesdir / 'site.cfg', './'])

    def build(self):
        self.run([
            'python',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python/usr/include/python3.6m:../../build/target/openblas/usr/include',
            f'-L../../build/target/python/usr/lib:../../build/target/openblas/usr/lib',
            f'-lpython3.6m',
        ])
