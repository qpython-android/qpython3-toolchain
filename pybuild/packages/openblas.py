from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class OpenBLAS(Package):
    source = GitSource('https://github.com/AIPYX/OpenBLAS.git', alias='openblas', branch='qpyc/0.2.21')
    patches = [
        #LocalPatch('0001-set-stderr'),
    ]

    skip_uploading = True
    re_configure = True

    def prepare(self):
        #self.run_with_env([])
        pass

    #make TARGET=ARMV7 HOSTCC=gcc CC=arm-linux-androideabi-gcc FC=arm-linux-androideabi-gfortran FFLAGS="--sysroot /home/QPY/android-ndk-r13b/platforms/android-23/arch-arm" CFLAGS="--sysroot /home/QPY/android-ndk-r13b/platforms/android-23/arch-arm" LDFLAGS="-L/home/QPY/android-ndk-r13b/platforms/android-23/arch-arm/usr/lib/ -L/home/QPY/android-ndk-r13b/toolchains/arm-linux-androideabi-4.9/arm-linux-androideabi/lib/ -static-libgfortran" PREFIX=/opt/OpenBLAS NETLIB_LAPACK_DIR=/home/QPY/qpyc/build/openblas/OpenBLAS/lapack-netlib libs
    def build(self):
        self.system(
            f'make PREFIX={self.destdir()}/usr ARM_SOFTFP_ABI=1 TARGET=ARMV7 HOSTCC=gcc CC=arm-linux-androideabi-gcc FC=arm-linux-androideabi-gfortran FFLAGS=\"--sysroot {self.env["ARCH_SYSROOT"]}/..\" CFLAGS=\"--sysroot {self.env["ARCH_SYSROOT"]}/..\" LDFLAGS=\"-L{self.env["ARCH_SYSROOT"]}/lib  -static-libgfortran -L{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib -lgfortran\" NETLIB_LAPACK_DIR=lapack-netlib libs netlib re_lapack shared'
            )
        #self.run(['cp', self.filesdir / 'fix.sh', './exports'])
        #self.system(['cd exports && bash fix.sh'])


        """
        self.run_with_env([
            'make',
            'TARGET=ARMV7',
            'HOSTCC=gcc',
            f'CC={self.env["CC"]} {self.env["CLANG_FLAGS_QPY"]}',
            f'FC=arm-linux-androideabi-gfortran -DANDROID -mandroid --sysroot {self.env["ARCH_SYSROOT"]}/..',
            f'LDFLAGS=-lm -lgcc -lc -ldl -L{self.env["ARCH_SYSROOT"]}/lib -static-libgfortran',
            f'AR={self.env["AR"]}',
            #'ARM_SOFTFP_ABI=1',
            'NETLIB_LAPACK_DIR=lapack-netlib',
            'libs',
            #'netlib',
            #'shared',
            ])

        self.run_with_env([
            'make',
            'TARGET=ARMV7',
            'HOSTCC=gcc',
            f'CC={self.env["CC"]} {self.env["CLANG_FLAGS_QPY"]}',
            f'FC=arm-linux-androideabi-gfortran -DANDROID -mandroid --sysroot {self.env["ARCH_SYSROOT"]}/..',
            f'LDFLAGS=-lm -lgcc -lc -ldl -L{self.env["ARCH_SYSROOT"]}/lib -static-libgfortran',
            f'AR={self.env["AR"]}',
            #'ARM_SOFTFP_ABI=1',
            'NETLIB_LAPACK_DIR=lapack-netlib',
            #'libs',
            #'netlib',
            'shared',
            ])
        """

        self.run_with_env(['make', 'install', f'PREFIX={self.destdir()}/usr'])
