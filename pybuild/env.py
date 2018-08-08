import os

target_arch = 'arm'
android_api_level = os.getenv('ANDROID_VER')

# Python optional modules.
# Available:
#  tinycc - Tiny cc compiler
#  bzip2 - enable the bz2 module and the bzip2 codec
#  xz - enable the lzma module and the lzma codec
#  openssl - enable the ssl module and SSL/TLS support for sockets
#  readline - enable the readline module and command history/the like in the REPL
#  ncurses - enable the curses module
#  sqlite - enable the sqlite3 module
#  gdbm - enable the dbm/gdbm modules
#  libffi - enable the ctypes module
#  zlib - enable the zlib module
#  expat - enable the pyexpat module
#  tools - some handy utility scripts from ./devscripts
packages = ('openssl', 'ncurses', 'readline', 'bzip2', 'xz', 'zlib', 'sqlite', 'gdbm', 'libffi', 'expat', 'tools')
# 3rd Python modules.
#py_packages = ('openblas','numpy','scipy')
py_packages = ('libzmq','pyzmq')

skip_build_py  = os.path.exists(".skip_build_py")
skip_build_py2  = os.path.exists(".skip_build_py2")
skip_build_py_module  = os.path.exists(".skip_build_py_module")

use_bintray = False
bintray_username = 'qpython-android'
bintray_repo = 'qpython3-core'
