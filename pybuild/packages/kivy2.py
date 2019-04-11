from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Kivy2(Package):
    source = GitSource('https://github.com/qpython3/kivy.git', alias='kivy2', branch='qpyc-1.10.1')
    patches = [
        #LocalPatch('0001-add-ftello64'),
    ]

    #use_gcc = True

    def prepare(self):
        #self.run(['cp', self.filesdir / 'site.cfg', './'])
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')

        JNIR = os.path.join(self.filesdir, '../pygamesdl2/jni')
        JNIL = os.path.join(self.filesdir, '../pygamesdl2/libs/armeabi-v7')
        JNIO = os.path.join(self.filesdir, '../pygamesdl2/obj/local/armeabi-v7a')
        self.system("find . -iname '*.pyx' -exec cython {} \;")

        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}:../../build/target/openblas/usr/include:{JNIR}',
            f'-L../../build/target/python{PY_BRANCH}/usr/lib:../../build/target/openblas/usr/lib:{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm:{self.filesdir}/libs/armeabi-v7a:{JNIL}:{JNIO}',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
