Python 3 Android
================

This is an experimental set of build scripts that will cross-compile the specific Python 3 for QPython3.


Prerequisites
-------------

Building requires:

1. Linux or macOS. Ubuntu 14.04, Arch Linux and macOS Sierra tested.
2. Android NDK r16 beta 2 installed and environment variable ``$ANDROID_NDK`` points to its root directory. NDK r14 or r15 may work yet not fully tested. NDk r13 or below is not supported.
3. git and python in $PATH. It's recommended to use the latest git-master to build python. Here are some ways to install the python:
* For Arch Linux users, install [python-git](https://aur.archlinux.org/packages/python-git) package from AUR
* For Homebrew users, run ```brew install python3 --HEAD```
* For MacPorts users, add [my MacPorts overlay](https://github.com/yan12125/macports-overlay) to ``sources.conf`` and run ```sudo port install python37```
* For other users, install 3.8 from [pyenv](https://github.com/yyuu/pyenv)

Running requires:

1. Android 5.0 (Lollipop, API 21) or above
2. arm, arm64, x86 or x86-64
3. A `busybox` binary at /data/local/tmp/busybox

Build
-----

1. `make clean` for good measure.
2. For every API Level/architecture combination you wish to build for:
   * Edit `env` to match your (desired) configuration.
   * `make` to build everything!


Installation
------------
TBD


SSL/TLS
-------
SSL certificates have old and new naming schemes. Android uses the old scheme yet the latest OpenSSL uses the new one. If you got ```CERTIFICATE_VERIFY_FAILED``` when using SSL/TLS in Python, you need to generating certificate names of the new scheme:
```
python ./python3/tools/c_rehash.py
```
Check SSL/TLS functionality with:
```
python ./python3/tools/ssl_test.py
```


Known Issues
------------
Please file a issue [to the issue list](https://github.com/qpython-android/qpython3-core/issues)



Others
---------------
Folked from [Python3-Android](https://github.com/rave-engine/python3-android)

Thanks the author and contributor: [Shizmob](https://github.com/Shizmob),(Chih-Hsuan Yen)[https://github.com/yan12125]

