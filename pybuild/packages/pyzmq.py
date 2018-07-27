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
            f'-L../../build/target/python/usr/lib:../../build/target/libzmq/lib',
            f'-lpython3.6m,zmq',
        ])
        self.run([
            'python',
            'setup.py',
            'build_py',
        ])
