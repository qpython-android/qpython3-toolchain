from ..source import GitSource
from ..package import Package
from ..patch import LocalPatch
from ..util import target_arch

import os

class OpenCV2(Package):
    source = GitSource('https://github.com/AIPYX/opencv.git', alias='opencv', branch='qpyc/3.4.3-openvino')
    patches = [
        #LocalPatch('0001-cross-compile'),
    ]

    def prepare(self):
        pass

    def build(self):
        PY_BRANCH = os.getenv('PY_BRANCH')
        PY_M_BRANCH = os.getenv('PY_M_BRANCH')
        ANDROID_SDK = os.getenv('ANDROID_SDK')
        SRC = self.source.source_dir
        self.system( 
        f"mkdir -p build && cd build && cmake -DTEST_BIG_ENDIAN=0 -DP4A=ON -DANDROID_ABI=armeabi-v7a -DANDROID_NATIVE_API_LEVEL=android-21 -DCMAKE_TOOLCHAIN_FILE={SRC}/platforms/android/android.toolchain.cmake "\
	    "-DPYTHON_INCLUDE_PATH=../../../build/target/python2/usr/include/python2.7 -DPYTHON_LIBRARY=../../../build/target/python2/usr/lib/libpython2.7.so "\
        "-DPYTHON_NUMPY_INCLUDE_DIR=../../numpy2/numpy/core/include "\
	    f"-DANDROID_EXECUTABLE={ANDROID_SDK}/tools/android "\
	    "-DBUILD_TESTS=OFF -DBUILD_PERF_TESTS=OFF -DBUILD_EXAMPLES=OFF -DBUILD_ANDROID_EXAMPLES=OFF "\
	    f"-DPYTHON_PACKAGES_PATH=. {SRC} &&"\
        "make opencv_python &&"\
        "cmake -DCOMPONENT=python -P ../cmake_install.cmake"
        )
