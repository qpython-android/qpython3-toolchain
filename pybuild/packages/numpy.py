from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class NumPy(Package):
    source = GitSource('https://github.com/AIPYX/numpy.git', alias='numpy', branch='qpyc/v1.14.3')
    patches = [
        LocalPatch('0001-cross-compile'),
        #LocalPatch('0001-add-ftello64'),
    ]

    use_gcc = True

    def prepare(self):
        self.run(['cp', self.filesdir / 'site.cfg', './'])

    def build(self):
        self.system(
            f'LD="arm-linux-androideabi-ld" python setup.py build_ext -I../../build/target/python/usr/include/python3.6m:../../build/target/openblas/usr/include -L../../build/target/python/usr/lib:../../build/target/openblas/usr/lib -lpython3.6m && python setup.py build_py',
        )
