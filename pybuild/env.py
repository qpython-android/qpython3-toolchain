import os

target_arch = 'arm'
android_api_level = os.getenv('ANDROID_VER')
target_arch_qpy= os.getenv('TARGET_ARCH_QPY')

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
packages = ('openssl', 'ncurses', 'readline', 'bzip2', 'zlib', 'sqlite', 'gdbm', 'libffi', 'expat', 'tools')
# 3rd Python modules.
py_packages = ('openblas','numpy',)

rebuild_py  = False

use_bintray = False
bintray_username = 'qpython-android'
bintray_repo = 'qpython3-core'
