from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch


class TinyCC(Package):
    source = GitSource('https://github.com/qpython-android/tinycc', alias='tinycc')
    patches = [
        LocalPatch('0001-Update-Makefile-for-cross-compile'),
        #LocalPatch('0001-TCC_ANDROID.patch'),
    ]

    re_configure = True
    use_gcc = True

    def prepare(self):
        self.run_with_env([
            './configure',
            '--prefix=/data/data/org.qpython.qpy/files',
            f'--sysroot={self.env["ARCH_SYSROOT"]}',
            f'--cc={self.env["CC"]}',
            f'--ar={self.env["AR"]}',
            f'--extra-cflags=-I{self.env["ARCH_SYSROOT"]}/include -D__ANDROID_API__=21 ',
            f'--extra-ldflags=--sysroot {self.env["ARCH_SYSROOT"]} -L. -D__ANDROID_API__=21 -fPIE -pie '
            '',
            '--cpu=armv7',
            '--disable-static',
            #'--enable-cross',
            #'--with-libgcc',
            #'--disable-OSX',
            #'--config-uClibc',
            #'-DTCC_ANDROID'
        ])

    def build(self):
        self.run(['make', 'cross-arm'])
        #self.run(['make', 'install', f'DESTDIR={self.destdir()}'])
