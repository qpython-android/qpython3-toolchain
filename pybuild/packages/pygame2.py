from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Pygame2(Package):
    source = GitSource('https://github.com/QPYPI/pygame-qpython.git', alias='pygame2', branch='qpyc-1.9.4')
    patches = [
        #LocalPatch('0001-add-ftello64'),
    ]

    #use_gcc = True

    def prepare(self):
        self.run(['cp', self.filesdir / 'Setup', './'])

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        JNIR = os.path.join(self.filesdir, '../kivy2/jni')
        JNIL = os.path.join(self.filesdir, '../kivy2/libs/armeabi-v7')
        JNIO = os.path.join(self.filesdir, '../kivy2/obj/local/armeabi-v7a')
        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}:../../build/target/openblas/usr/include:{JNIR}:{JNIR}/png:{JNIR}/jpeg:{JNIR}/sdl/include:{JNIR}/sdl_mixer:{JNIR}/sdl_ttf:{JNIR}/sdl_image',
            f'-L../../build/target/python{PY_BRANCH}/usr/lib:{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm:{JNIL}:{JNIO}',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m,z',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])

    def fresh(self):
        return True
