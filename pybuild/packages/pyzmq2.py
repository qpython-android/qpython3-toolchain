from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class PyZMQ2(Package):
    source = GitSource('https://github.com/qpython3/pyzmq.git', alias='pyzmq2', branch='qpyc/17.1.0')
    patches = [
        #LocalPatch(''),
    ]

    def prepare(self):
        self.run(['cp', self.filesdir / 'setup.cfg', './'])

    def build(self):
        self.run([
            'python2',
            'setup.py',
            'build_ext',
            f'-I../../build/target/python2/usr/include/python2.7:../../build/target/libzmq/include',
            f'-L../../build/target/python2/usr/lib'\
            f':../../build/target/libzmq/lib'\
            f':{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a'\
            f':{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a'\
            f':{self.env["ANDROID_NDK"]}/toolchains/renderscript/prebuilt/linux-x86_64/platform/arm',
            f'-lpython2.7,zmq,gnustl_static,atomic',
        ])
        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])

    def fresh(self):
        return True
