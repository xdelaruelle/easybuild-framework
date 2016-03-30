#!/bin/bash

set -e

if [ $# -ne 2 ]; then
    echo "Usage: $0 <name>-<version> <prefix>"
    exit 1
fi
PKG=$1
PREFIX=$2

PKG_NAME=`echo $PKG | sed 's/-[^-]*$//g'`
PKG_VERSION=`echo $PKG | sed 's/.*-//g'`

if [ x$PKG_NAME == 'xmodules' ]; then
    PKG_URL="http://prdownloads.sourceforge.net/modules/${PKG}.tar.gz"
    export PATH=$PREFIX/Modules/$PKG_VERSION/bin:$PATH
    export MOD_INIT=$HOME/Modules/$PKG_VERSION/init/bash

elif [ x$PKG_NAME == 'xlua' ]; then
    PKG_URL="http://downloads.sourceforge.net/project/lmod/${PKG}.tar.gz"
    CONFIG_OPTIONS='--with-static=yes'
    export PATH=$PREFIX/bin:$PATH

elif [ x$PKG_NAME == 'xLmod' ]; then
    PKG_URL="https://github.com/TACC/Lmod/archive/${PKG_VERSION}.tar.gz"
    export PATH=$PREFIX/lmod/$PKG_VERSION/libexec:$PATH
    export MOD_INIT=$HOME/lmod/$PKG_VERSION/init/bash

elif [ x$PKG_NAME == 'xmodules-tcl' ]; then
    PKG_URL="https://sourceforge.net/code-snapshots/git/m/mo/modules/modules-tcl.git/modules-${PKG}.zip"
    export PATH=$PREFIX/modules-${PKG}:$PATH
else
    echo "ERROR: Unknown package name '$PKG_NAME'"
    exit 2
fi

echo "Installing ${PKG} @ ${PREFIX}..."
wget ${PKG_URL}
if [ x$PKG_NAME == 'xmodules-tcl' ]; then
    unzip modules-${PKG}.zip
    cp -a modules-${PKG} $PREFIX
else
    tar xfz *${PKG_VERSION}.tar.gz && cd ${PKG}
    ./configure $CONFIG_OPTIONS --prefix=$PREFIX && make && make install
fi
