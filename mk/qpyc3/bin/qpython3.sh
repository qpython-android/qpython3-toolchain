#!/system/bin/sh
DIR=${0%/*}
. $DIR/init.sh && $DIR/python3 "$@" && $DIR/end.sh

