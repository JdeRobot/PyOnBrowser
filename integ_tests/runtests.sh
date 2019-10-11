#!/bin/sh

export PASS=pass

usage(){
	echo "usage: runtests.sh [workdir]" 1>&2;
	exit 1
}
dotest(){
	dirtest=$1
	jsexe=`mktemp`
	nametest=$2
	namepy=`echo $dirtest/*.py`
	if ! test -f $namepy; then
		echo bad test $dirtest no py file
		return
	fi
	python3 main.py --emulate $dirtest --outfile $jsexe $namepy
	js $jsexe > $namepy.out 2>&1
	for i in $dirtest/*.out.ok; do
		nameout=`echo $i|sed 's/\.ok$//g'`
		if cmp -s $nameout $nameout.ok; then
			rm $i
		else
			echo for `basename $namepy` $nameout is not $workdir/integ_tests/$t/`basename $nameout`.ok
			false
			return
		fi
	done
	echo $nametest pass
}

case $# in
0)
	workdir=`pwd`'/..'
	;;
1)
	workdir=$1
	;;
*)
	usage
esac

cd $workdir/integ_tests

for t in *_test; do
	if ! test -d $t; then
		continue
	fi
	dirtest=`mktemp -d`
	cp -a $workdir/integ_tests/$t/* $dirtest
	cd $workdir;
	if ! dotest $dirtest $t; then
		export PASS=fail
	fi
done
echo tests $PASS;
if [ $PASS != pass ]; then
	exit 1
fi
exit 0