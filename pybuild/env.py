import os

target_arch = 'arm'
android_api_level = 21
crystax_target_arch=os.getenv('CRYSTAX_TARGET_ARCH')

# Python optional modules.
# Available:
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
#packages = ('tinycc', 'openssl', 'ncurses', 'readline', 'sqlite', 'bzip2', 'xz', 'gdbm', 'libffi', 'zlib', 'expat', 'tools', )
packages = ('openblas', 'openssl', 'ncurses', 'readline', 'sqlite', 'bzip2', 'gdbm', 'libffi', 'zlib', 'expat', 'tools')
py_packages = ('numpy',)

rebuild_py  = False

use_bintray = False
bintray_username = 'qpython-android'
bintray_repo = 'qpython3-core'
