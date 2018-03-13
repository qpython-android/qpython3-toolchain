#!/system/bin/sh
DIR=${0%/*}
if [ -z "$1" ]; then
    . $DIR/init.sh && $DIR/python3 "$@" && $DIR/bend.sh
else
    is_web=`grep "#qpy:webapp" $1`
    is_qapp1=`grep "#qpy:qpyapp" $1`
    is_qapp2=`grep "#qpy:qpysrv" $1`

    if [ -z "${is_web}" ]  && [ -z "${is_qapp1}" ] && [ -z "${is_qapp2}" ]; then
        . $DIR/init.sh && $DIR/python3 "$@" && $DIR/bend.sh
    else
        . $DIR/init.sh && $DIR/python3 "$@" && $DIR/send.sh
    fi
fi
