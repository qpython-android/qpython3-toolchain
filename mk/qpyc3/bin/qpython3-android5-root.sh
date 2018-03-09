#!/system/bin/sh
DIR=${0%/*}
test=$DIR'/init.sh && '$DIR'/python3-android5 '"$@"' && '$DIR'/end.sh'
cat $DIR/init.sh > $DIR/python3-android5-root
echo '\n' >> $DIR/python3-android5-root
echo $test >> $DIR/python3-android5-root
chmod 755 $DIR/python3-android5-root
su -c $DIR/python3-android5-root
