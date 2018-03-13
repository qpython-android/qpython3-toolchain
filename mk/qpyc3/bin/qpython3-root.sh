#!/system/bin/sh
DIR=${0%/*}
if [ -z "$1" ]; then
    test=$DIR'/init.sh && '$DIR'/python3 && '$DIR'/bend.sh'
else
    is_web=`grep "#qpy:webapp" $1`
    is_qapp1=`grep "#qpy:qpyapp" $1`
    is_qapp2=`grep "#qpy:qpysrv" $1`

    if [ -z "${is_web}" ]  && [ -z "${is_qapp1}" ] && [ -z "${is_qapp2}" ]; then
        test=$DIR'/init.sh && '$DIR'/python3 '"$@"' && '$DIR'/bend.sh'
    else
        test=$DIR'/init.sh && '$DIR'/python3 '"$@"' && '$DIR'/send.sh'
    fi
fi


cat $DIR/init.sh > $DIR/python3-root
echo '\n' >> $DIR/python3-root
echo $test >> $DIR/python3-root
chmod 755 $DIR/python3-root
su -c $DIR/python3-root
