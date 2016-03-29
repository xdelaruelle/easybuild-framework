#!/bin/bash

set -e

if [ $# -ne 2 ]; then
    echo "Usage: $0 <name>-<version> <prefix>"
    exit 1
fi
PKG=$1
PREFIX=$2

PKG_NAME=`echo $PKG | cut -f1 -d'-'`
PKG_VERSION=`echo $PKG | cut -f2 -d'-'`

if [ x$PKG_NAME == 'xmodules' ]; then
    PKG_URL='http://prdownloads.sourceforge.net/modules/'
    export PATH=$PREFIX/Modules/$PKG_VERSION/bin:$PATH

elif [ x$PKG_NAME == 'xlua' ]; then
    PKG_URL='http://downloads.sourceforge.net/project/lmod/'
    CONFIG_OPTIONS='--with-static=yes'
    export PATH=$PREFIX/bin:$PATH

elif [ x$PKG_NAME == 'xLmod' ]; then
    PKG_URL='https://github.com/TACC/Lmod/archive/'
    export PATH=$PREFIX/lmod/$PKG_VERSION/libexec:$PATH
else
    echo "ERROR: Unknown package name '$PKG_NAME'"
    exit 2
fi

echo "Installing ${PKG} @ ${PREFIX}..."
wget ${PKG_URL}/${PKG}.tar.gz
tar xfz ${PKG}.tar.gz && cd ${PKG}
./configure $CONFIG_OPTIONS --prefix=$PREFIX && make && make install
