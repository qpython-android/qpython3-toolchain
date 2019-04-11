from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class PyZMQ(Package):
    source = GitSource('https://github.com/qpython3/pyzmq.git', alias='pyzmq', branch='qpyc/17.1.0')
    patches = [
        #LocalPatch(''),
    ]

    def prepare(self):
        self.run(['cp', self.filesdir / 'setup.cfg', './'])

    def build(self):
        self.run([
            'python',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python/usr/include/python3.6m:../../build/target/libzmq/include',
            f'-L../../build/target/python/usr/lib:../../build/target/libzmq/lib:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a:{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a',
            f'-lpython3.6m,zmq,gnustl_static,atomic',
        ])
        self.run([
            'python',
            'setup.py',
            'build_py',
        ])

    def fresh(self):
        return True
