from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class OpenBLAS(Package):
    source = GitSource('https://github.com/AIPYX/OpenBLAS.git', alias='openblas', branch='qpyc/0.2.21')
    patches = [
        LocalPatch('0001-cross-compile'),
        #LocalPatch('0001-Disable-stderr-in-blas_server'),
    ]

    skip_uploading = True
    re_configure = True

    def prepare(self):
        pass

    def build(self):
        self.system(
            #f'make PREFIX={self.destdir()}/usr ARM_SOFTFP_ABI=1 TARGET=ARMV7 HOSTCC=gcc CC=arm-linux-androideabi-gcc FC=arm-linux-androideabi-gfortran FFLAGS=\"--sysroot {self.env["ARCH_SYSROOT"]}/..\" CFLAGS=\"--sysroot {self.env["ARCH_SYSROOT"]}/.. -I{self.env["ANDROID_NDK"]}/sysroot/usr/include/ -I{self.env["ANDROID_NDK"]}/sysroot/usr/include/arm-linux-androideabi/\" LDFLAGS=\"-L{self.env["ARCH_SYSROOT"]}/lib -L{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a\" NETLIB_LAPACK_DIR=lapack-netlib libs netlib shared'
            f'make PREFIX={self.destdir()}/usr ARM_SOFTFP_ABI=1 TARGET=ARMV7 HOSTCC=gcc CC=arm-linux-androideabi-gcc FC=arm-linux-androideabi-gfortran FFLAGS=\"--sysroot {self.env["ARCH_SYSROOT"]}/..\" CFLAGS=\"--sysroot {self.env["ARCH_SYSROOT"]}/.. -D__ANDROID_API__=21 -I{self.env["ANDROID_NDK"]}/sysroot/usr/include/ -I{self.env["ANDROID_NDK"]}/sysroot/usr/include/arm-linux-androideabi/\" LDFLAGS=\"-L{self.env["ARCH_SYSROOT"]}/lib -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -lgfortran\" NETLIB_LAPACK_DIR=lapack-netlib'
            )
        self.run_with_env(['make', 'install', f'PREFIX={self.destdir()}/usr'])
        self.system(
            f'rm {self.destdir()}/usr/lib*so*'
        )
