from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class SciPy(Package):
    source = GitSource('https://github.com/AIPYX/scipy.git', alias='scipy', branch='qpyc/v1.1.0')
    patches = [
        LocalPatch('0001-cross-compile'),
    ]

    use_gcc = True

    def prepare(self):
        self.run(['cp', self.filesdir / 'site.cfg', './'])

    def build(self):
        import os,sys
        self.system( 
            f'python setup.py build_ext -I../../build/target/python/usr/include/python3.6m:../../build/target/openblas/usr/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi/include -L../../build/target/python/usr/lib:../../build/target/openblas/usr/lib:../numpy/build/temp.linux-x86_64-3.6 -lopenblas,python3.6m,m,gfortran' 
        )
        self.run([
            'python',
            'setup.py',
            'build_py',
        ])
