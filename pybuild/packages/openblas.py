from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class OpenBLAS(Package):
    source = GitSource('https://github.com/AIPYX/OpenBLAS.git', alias='openblas', branch='qpyc/0.2.21')
    patches = [
        LocalPatch('0001-set-stderr'),
    ]

    def prepare(self):
        #self.run_with_env([])
        pass

    def build(self):
        self.run_with_env([
            'make',
            'TARGET=ARMV7',
            'ONLY_CBLAS=1',
            f'AR={self.env["AR"]}',
            f'CC={self.env["CC"]} {self.env["CLANG_FLAGS_QPY"]}',
            'HOSTCC=gcc',
            'ARM_SOFTFP_ABI=1',
            ])

        self.run_with_env(['make', 'install', f'PREFIX={self.destdir()}/usr'])
