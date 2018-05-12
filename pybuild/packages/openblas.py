from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class OpenBLAS(Package):
    source = GitSource('https://github.com/AIPYX/OpenBLAS.git', alias='openblas', branch='qpyc/0.2.21')
    patches = [
        #LocalPatch('0001-set-stderr'),
    ]

    skip_uploading = True
    re_configure = True

    def prepare(self):
        #self.run_with_env([])
        pass

    def build(self):
        import os
        self.run_with_env([
            'make',
            'TARGET=ARMV7',
            'ONLY_CBLAS=1',
            f'AR={self.env["AR"]}',
            f'CC={self.env["CC"]} {self.env["CLANG_FLAGS_QPY"]}',
            f'FC=arm-linux-androideabi-gfortran -DANDROID -mandroid --sysroot {self.env["ARCH_SYSROOT"]}/..',
            f'LDFLAGS=-lm -lgcc -lc -ldl',
            'HOSTCC=gcc',
            'ARM_SOFTFP_ABI=1',
            #'libs',
            ])

        self.run_with_env(['make', 'install', f'PREFIX={self.destdir()}/usr'])
