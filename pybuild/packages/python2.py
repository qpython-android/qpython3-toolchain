import os
from .. import env
from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch, RemotePatch
from ..util import target_arch


class Python2(Package):
    source = GitSource('https://github.com/qpython-android/cpython/', branch='qpyc-2.7.15', alias='cpython2')
    patches = [
        # https://bugs.python.org/issue29440
        LocalPatch('0001-py-cross-compile1'),
        LocalPatch('0002-py-cross-compile2'),
        LocalPatch('0002-Update-build-info'),
        LocalPatch('0003-fix-readline-issues'),
        LocalPatch('0001-disabled-readline'),
        LocalPatch('0001-fix-gethostbyaddr'),
        LocalPatch('0001-fix-default-decoding'),
        LocalPatch('0001-python-lib-for-qpy'),
        #RemotePatch('https://github.com/python/cpython/pull/139.patch'),
    ]

    dependencies = list(env.packages)

    skip_uploading = True

    def __init__(self):
        super(Python2, self).__init__()

        self.env['CONFIG_SITE'] = self.filesdir / 'config.site'
        self.env['CFLAGS'] = os.getenv('CLANG_FLAGS_BASE')
        self.env['CROSS_COMPILE_TARGET'] = 'yes'
        self.env['INSTSONAME'] = 'libpython2.7.so' 
        #self.env['_PYTHON_HOST_PLATFORM'] = "linux-x86_64" 
        self.env['CROSS_COMPILE_TARGET'] = "yes"


    def prepare(self):
        self.run(['autoreconf', '--install', '--verbose', '--force'])

        #self.env['CONFIG_SITE'] = self.filesdir / 'config.site'
        self.run_with_env([
            './configure',
            '--prefix=/usr',
            '--host=' + target_arch().ANDROID_TARGET,
            # CPython requires explicit --build
            '--build=x86_64-linux-gnu',
            '--enable-unicode=ucs4',
            '--disable-ipv6',
            '--with-system-ffi',
            '--with-system-expat',
            '--without-ensurepip',
            '--enable-shared',
        ])
        #self.run(['echo', '"#define __ANDROID__"', '>>', 'pyconfig.h'])

    def build(self):
        self.run(['make'])
        self.run(['make', 'altinstall', f'DESTDIR={self.destdir()}'])

    def fresh(self):
        return True
