from .. import env
from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch, RemotePatch
from ..util import target_arch


class Python(Package):
    source = GitSource('https://github.com/qpython-android/cpython/', branch='qpyc-3.6.4') 
    patches = [
        # https://bugs.python.org/issue29440
        RemotePatch('https://bugs.python.org/file46517/gdbm.patch'),
        LocalPatch('cppflags'),
        LocalPatch('skip-build'),
        LocalPatch('py36-0001-Up-configure'),
        LocalPatch('py36-pyport-undef-HAVE_LANGINFO_H'),
        LocalPatch('py36-0001-Update-compile-flag'),
        #LocalPatch('py36-0001-Remove-readline'),
        RemotePatch('https://github.com/python/cpython/pull/139.patch'),
    ]

    dependencies = list(env.packages)

    skip_uploading = True

    def __init__(self):
        super(Python, self).__init__()

        self.env['CONFIG_SITE'] = self.filesdir / 'config.site'

    def prepare(self):
        self.run(['autoreconf', '--install', '--verbose', '--force'])

        self.run_with_env([
            './configure',
            '--prefix=/usr',
            '--host=' + target_arch().ANDROID_TARGET,
            # CPython requires explicit --build
            '--build=x86_64-linux-gnu',
            '--disable-ipv6',
            '--with-system-ffi',
            '--with-system-expat',
            '--without-ensurepip',
        ])
        self.run(['echo', '"#define __ANDROID__"', '>>', 'pyconfig.h'])

    def build(self):
        self.run(['make'])
        self.run(['make', 'altinstall', f'DESTDIR={self.destdir()}'])
