target_arch = 'arm'
android_api_level = 21
crystax_target_arch='armeabi-v7a'

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
packages = ( 'openssl', 'ncurses', 'readline', 'sqlite', 'bzip2', 'gdbm', 'libffi', 'zlib', 'expat', 'tools', )

use_bintray = False
bintray_username = 'yan12125'
bintray_repo = 'cpython-bin-deps-android'
