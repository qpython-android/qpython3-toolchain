from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class Pillow2(Package):
    source = GitSource('https://github.com/QPYPI/pillow.git', alias='pillow2', branch='qpyc/5.2.0')
    patches = [
        #LocalPatch('0001-cross-compile'),
    ]

    def prepare(self):
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        JNIR = os.path.join(self.filesdir, '../pygamesdl2/jni')
        JNIL = os.path.join(self.filesdir, '../pygamesdl2/libs/armeabi-v7')
        JNIO = os.path.join(self.filesdir, '../pygamesdl2/obj/local/armeabi-v7a')
        BILD = os.path.join(self.destdir(), '..')

        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python{PY_BRANCH}/usr/include/python{PY_BRANCH}.{PY_M_BRANCH}'\
            ':../../build/target/openblas/usr/include'\
            f':{JNIR}/jpeg'\
            f':{JNIR}/png'\
            f':{JNIR}/libwebp/src'\
            f':{BILD}/zlib/usr/include'\
            f':{JNIR}/freetype/include',
            f'-L../../build/target/python{PY_BRANCH}/usr/lib'\
            ':../../build/target/openblas/usr/lib'\
            f':{BILD}/zlib/usr/lib'\
            f':{JNIO}'\
            f':{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm',
            f'-lpython{PY_BRANCH}.{PY_M_BRANCH},m',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
