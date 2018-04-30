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
            '--prefix=/data/data/org.qpython.qpy.community/files',
            f'--sysroot={self.env["ARCH_SYSROOT"]}',
            f'--cc={self.TOOL_PREFIX}/bin/arm-linux-androideabi-gcc',
            f'--ar={self.TOOL_PREFIX}/bin/arm-linux-androideabi-ar',
            f'--extra-cflags=-I{self.env["UNIFIED_SYSROOT"]}/include -I{self.env["UNIFIED_SYSROOT"]}/include/arm-linux-androideabi -D__ANDROID_API__=21 ',
            f'--extra-ldflags= --sysroot {self.env["ARCH_SYSROOT"]} -L{self.env["ARCH_SYSROOT"]}/lib -L. -D__ANDROID_API__=21 -fPIE -pie '
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
