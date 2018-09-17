from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

class SciPy2(Package):
    source = GitSource('https://github.com/AIPYX/scipy.git', alias='scipy2', branch='qpyc/v1.1.0')
    patches = [
        LocalPatch('0001-cross-compile'),
    ]

    use_gcc = True

    def prepare(self):
        self.run(['cp', self.filesdir / 'site.cfg', './'])

    def build(self):
        import os,sys
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        self.system( 
            f'XCXX=\"clang++ -fno-integrated-as -femulated-tls -target arm-linux-androideabi -marm -mfpu=vfp -mfloat-abi=softfp \" LDFLAGS=\" -shared -DANDROID --sysroot {self.env["ANDROID_NDK"]}/platforms/android-21/arch-arm -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L../../build/target/python2/usr/lib -L../../build/target/openblas/usr/lib -L../numpy2/build/temp.linux-x86_64-2.7 \" python2 setup.py build_ext -I../../build/target/python2/usr/include/python2.7:../../build/target/openblas/usr/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -L../../build/target/python2/usr/lib:../../build/target/openblas/usr/lib:../numpy2/build/temp.linux-x86_64-3.6:{self.env["ANDROID_NDK_GFORTRAN"]}/platforms/android-21/arch-arm/usr/lib:{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a -lopenblas,python2.7,gcc' 
        )
        self.system( 
            f'XCXX=\"clang++ -fno-integrated-as -femulated-tls -target arm-linux-androideabi -marm -mfpu=vfp -mfloat-abi=softfp \" LDFLAGS=\" -shared -DANDROID --sysroot {self.env["ANDROID_NDK"]}/platforms/android-21/arch-arm -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L../../build/target/python2/usr/lib -L../../build/target/openblas/usr/lib\ -L../numpy2/build/temp.linux-x86_64-2.7" python2 setup.py build_clib -I../../build/target/python2/usr/include/python2.7:../../build/target/openblas/usr/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -L../../build/target/python2/usr/lib:../../build/target/openblas/usr/lib:../numpy2/build/temp.linux-x86_64-3.6:{self.env["ANDROID_NDK_GFORTRAN"]}/platforms/android-21/arch-arm/usr/lib:{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a -lopenblas,python2.7,gcc' 
        )

        self.system( 
            f'XCXX=\"clang++ -fno-integrated-as -femulated-tls -target arm-linux-androideabi -marm -mfpu=vfp -mfloat-abi=softfp \" LDFLAGS=\" -shared -DANDROID --sysroot {self.env["ANDROID_NDK"]}/platforms/android-21/arch-arm -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L../../build/target/python2/usr/lib -L../../build/target/openblas/usr/lib\" python2 scipy/_lib/setup.py build_ext -I../../build/target/python2/usr/include/python2.7:../../build/target/openblas/usr/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -L../../build/target/python2/usr/lib:../../build/target/openblas/usr/lib:../numpy2/build/temp.linux-x86_64-3.6:{self.env["ANDROID_NDK_GFORTRAN"]}/platforms/android-21/arch-arm/usr/lib:{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a -lopenblas,python2.7,gcc' 
        )

        self.system( 
            f'XCXX=\"clang++ -fno-integrated-as -femulated-tls -target arm-linux-androideabi -marm -mfpu=vfp -mfloat-abi=softfp \" LDFLAGS=\" -shared -DANDROID --sysroot {self.env["ANDROID_NDK"]}/platforms/android-21/arch-arm -L{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L../../build/target/python2/usr/lib -L../../build/target/openblas/usr/lib -L../numpy2/build/temp.linux-x86_64-2.7\" python2 scipy/special/setup.py build_ext -I../../build/target/python2/usr/include/python2.7:../../build/target/openblas/usr/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/include:{self.env["ANDROID_NDK"]}/sources/cxx-stl/gnu-libstdc++/4.9/libs/armeabi-v7a/include -L../../build/target/python2/usr/lib:../../build/target/openblas/usr/lib:../numpy2/build/temp.linux-x86_64-3.6:{self.env["ANDROID_NDK_GFORTRAN"]}/platforms/android-21/arch-arm/usr/lib:{self.env["ANDROID_NDK_GFORTRAN"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/arm-linux-androideabi/lib/armv7-a -L{self.env["ANDROID_NDK"]}/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/lib/gcc/arm-linux-androideabi/4.9.x/armv7-a -lopenblas,python2.7,gcc' 
        )


        self.run([
            'python2',
            'setup.py',
            'build_py',
        ])
